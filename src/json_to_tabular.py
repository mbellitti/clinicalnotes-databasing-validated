import sys

sys.path.append("/projectnb/vkolagrp/bellitti/clinicalnotes-databasing-validated/src")

from pathlib import Path
from pydantic import BaseModel, ValidationError
from tqdm import tqdm
import json_repair

import polars as pl

from pydantic import BaseModel, ConfigDict
import json
from nbse_report_schema_minimal import Report

from typing import Type
import re

base_path = Path("/projectnb/vkolagrp/bellitti/clinicalnotes-databasing-validated/")

json_dir = base_path / "results/tabular_extracted_smaller"

log_file = base_path / "logs/validation_failures.log"


def remove_think_content(text: str) -> str:
    """
    Remove all content (including newlines) between <think> and </think> tags.
    The tags themselves are also removed.

    Probably not needed, we are using Qwen3 in non-thinking mode.
    """
    pattern = re.compile(r"<think>.*?</think>", re.DOTALL)
    return pattern.sub("", text)


def remove_triple_backtick_lines(text: str) -> str:
    """
    Remove lines that contain three backticks, which is how Qwen marks that it is producing code.
    Useful to make parsing into a python dictionary easier.
    """
    lines = text.splitlines()
    cleaned = [line for line in lines if "```" not in line]
    return "\n".join(cleaned)


def validate_and_clean_data(data: dict, model: Type[BaseModel]) -> dict:
    """
    Validates a dictionary against a Pydantic model and sets invalid fields to None.

    Args:
        data (dict): The dictionary containing the data to validate.
        model (Type[BaseModel]): The Pydantic BaseModel to validate against.

    Returns:
        dict: The modified dictionary with invalid fields set to None.
    """
    
    cleaned_data = (
        data.copy()
    )  # Create a copy to avoid modifying the original dict during iteration

    try:
        return model.model_validate(cleaned_data)

    except ValidationError as e:
        # Iterate over each validation error to find the field name
        for error in e.errors():
            field_name = error["loc"][0]
            cleaned_data[field_name] = None

            with log_file.open("a", encoding="utf-8") as log:
                log.write(f"  -> Invalid field: '{field_name}'. Setting to None.\n")

        return model.model_validate(cleaned_data)


def load_json(file_path: Path) -> BaseModel | None:
    try:
        with open(file_path) as FILE:

            text = FILE.read()

            # text = remove_think_content(text)
            text = remove_triple_backtick_lines(text)

            text = json_repair.loads(text) # this always outputs valid json, it might still not comply with the schema
            # text = json.loads(
                # text
            # )  # this always outputs valid json, it might still not comply with the schema

            return text

    except Exception as e:
        with log_file.open("a", encoding="utf-8") as log:
            log.write(f"{file_path.name}: {e}\n")

        return None


def extract_id(s) -> int:
    # Extract VAC from string
    match = re.search(r"VAC[ _\.]*(\d+)", s)

    if match is None:
        raise ValueError(f"Could not match ID from filename {s}")
    else:
        return int(match.group(1))


def main():

    results = []

    for jsonfile in tqdm(list(json_dir.glob("*.json"))):

        with log_file.open("a", encoding="utf-8") as log:
            log.write(f"{jsonfile.name}\n")

        result = load_json(jsonfile)

        if result is None:
            print(f"Empty file {jsonfile}")
            continue

        result = validate_and_clean_data(result, Report)

        result = result.model_dump()

        result["filename"] = jsonfile.name
        
        result["VAC"] = extract_id(jsonfile.name)

        results.append(result)

    df = pl.DataFrame(results)

    df = df.with_columns(
        pl.col("completed").cast(pl.Date),
    ).drop('vac') # overwrite extracted vac column with one parsed by the filename

    df.write_parquet(base_path/"results/NBSE_tabulated.parquet")

if __name__ == "__main__":
    main()
