# Databasing clinical notes via local LLM

[![DOI](https://zenodo.org/badge/1046313758.svg)](https://doi.org/10.5281/zenodo.19362131)

This project uses an LLM to extract tabular data from Neurobehavioral State
Examination (NBSE) reports. While it does not use guided decoding, it still
provides the LLM with a JSON schema automatically generated from a pydantic
class.

This project uses `uv` to manage the python environment; whenever you need to
run a script that is aware of the python environment, make sure to use `uv
run`. For example:
```
$ uv run src/extract_tabular.py
```

The Bash scripts in the `scripts` directory are set up to be either run locally (if
you have a GPU) or submitted to SCC, so you can do either:
```
$ scripts/extract_tabular.sh # run locally
```
or 
```
$ qsub scripts/extract_tabular.sh # submit to SCC, edit script to request appropriate resources
```

Make sure you're loading cuda/12.8 if you're going to run the LLM. This is
automatically handled by the Bash scripts. 
