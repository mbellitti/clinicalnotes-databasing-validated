import sys

sys.path.append("../src")

from pathlib import Path
from tqdm import tqdm
import polars as pl

import requests
from ratelimit import limits, sleep_and_retry


@sleep_and_retry
@limits(calls=20, period=1)  # RxNorm has a limit of 20 calls per second
def standardize_drug_name(search_term: str) -> list:
    approx_url = "https://rxnav.nlm.nih.gov/REST/approximateTerm.json"
    related_url = "https://rxnav.nlm.nih.gov/REST/rxcui/{rxcui}/related.json"

    params = {
        "format": ".json",
        "term": search_term,
        "option": 1,  # include all active concepts, necessary for approximate search
        "maxEntries": 1,  # do not return more than these many approximate matches, it may return fewer
    }

    resp = requests.get(approx_url, params=params)
    resp.raise_for_status()

    candidates = (
        resp.json().get("approximateGroup").get("candidate")
    )  # This is always a list, even for a single best match

    if candidates is None:
        return []

    rxcui = candidates[0]["rxcui"]  # get the top candidate

    related = requests.get(related_url.format(rxcui=rxcui), params={"tty": ["IN"]})
    related.raise_for_status()

    # this is always an ingredient, so the name is the standardized ingredient name
    # it may be a list of ingredients for a multi-ingredient drug
    ingredients = (
        related.json()
        .get("relatedGroup")
        .get("conceptGroup")[0]
        .get("conceptProperties")
    )

    if ingredients is None:
        return []
    else:
        ingredient_names = [ingredient["name"] for ingredient in ingredients if ingredient is not None]

    print(search_term)
    print(ingredient_names)
    print()

    return ingredient_names


def main():
    base_path = Path("/projectnb/vkolagrp/bellitti/clinicalnotes-databasing-validated")
    tabular_path = base_path / "results/NBSE_tabulated.parquet"

    tabular = (
        pl.read_parquet(tabular_path)
        .select("VAC", "medications")
        .explode("medications")
    )

    df = tabular.with_columns(
            pl.col("medications")
            .map_elements(standardize_drug_name, return_dtype=pl.List(pl.String))
            .alias("standard_ingredient")
        ).rename({'medications':'medication'}).explode('standard_ingredient')

    df.write_parquet(base_path / "results/medications_tabulated.parquet")


if __name__ == "__main__":
    main()
