#! /bin/bash -l

# This script is set up so that you can either qsub it or run it interactively.

# Make sure you're logged in to huggingface before running, if you're not sure
# you should login using "huggingface-cli login" before running this script

# Requesting resources from SCC
#$ -P vkolagrp
#$ -l h_rt=24:00:00
#$ -pe omp 8
#$ -l mem_per_core=2G
#$ -l gpus=2
#$-l gpu_c=8 # GPU capability, must be at least 8 for this project
# -l gpu_type=H200 
#$ -e logs/$JOB_ID.stderr
#$ -o logs/$JOB_ID.stdout

set -e

module load python3/3.12.4
module load cuda/12.8

# Cache for huggingface models
export HF_HOME=/projectnb/vkolagrp/bellitti/.cache/huggingface

# If this env var is set to 1, vLLM will skip the peer-to-peer check,
# and trust the driver's peer-to-peer capability report.
export VLLM_SKIP_P2P_CHECK=1

uv run src/extract_tabular.py