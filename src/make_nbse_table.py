# Look at the specified directory, get all the txt files,
# put them in a single table with these columns:
#
# VAC: int
# filename: name of txt file 
# full_text: full text of the report
# nchars: length of the report, number of characters

import re
import polars as pl
from pathlib import Path
from tqdm import tqdm

base_path = Path('/projectnb/vkolagrp/bellitti/clinicalnotes-databasing-validated')

txt_dir = base_path / 'data/NBSE_txt'


def extract_id(s) -> int:
    # Extract VAC from string
    match = re.search(r"VAC[_\s\.]*(\d+)", s)

    if match is None:
        raise ValueError(f"Could not match ID from filename {s}")
    else:
        return int(match.group(1))

nbse = []

for filename in tqdm(txt_dir.glob('*.txt')):

    case_dict = {}

    vac_id = extract_id(filename.stem)

    case_dict['VAC'] = vac_id

    case_dict['filename'] = filename.name

    with open(filename) as f:
        case_dict['full_text'] = f.read()
    
    case_dict['nchars'] = len(case_dict['full_text'])

    nbse.append(case_dict)

nbse_df = pl.DataFrame(nbse).sort('VAC')

nbse_df.write_parquet(base_path / 'results/full_reports.parquet')