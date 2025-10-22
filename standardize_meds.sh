#! /bin/bash -l

# This script is set up so that you can either qsub it or run it interactively.

#$ -P vkolagrp
#$ -l h_rt=12:00:00
#$ -pe omp 16
#$ -l avx2
#$ -l mem_per_core=1G

#$ -e logs/$JOB_ID.stderr
#$ -o logs/$JOB_ID.stdout

set -e

module load python3/3.12.4

uv run src/standardize_meds.py