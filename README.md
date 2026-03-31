# Databasing clinical notes via local LLM
Using an LLM to extract tabular data from clinical notes, according to a validated JSON schema for reliability.

This project uses `uv`; whenever you need to run a script that is aware of the python environment, make sure to use `uv run`. For example:

```
$ uv run src/extract_tabular.py
```

The scripts in the `scripts` directory are set up to be either run locally (if you have a GPU) or submitted to SCC, so you can do either:
```
$ scripts/extract_tabular.sh # run locally
```
or 
```
$ qsub scripts/extract_tabular.sh # submit to SCC, edit script to request appropriate resources
```


Make sure you're loading cuda/12.8 if you're going to run the LLM. This is automatically handled by the scripts, so you can just use those.