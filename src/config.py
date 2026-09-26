"""Project configuration: file paths, data provenance and the random seed."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"
TABLE_DIR = OUTPUT_DIR / "tables"
RESULTS_DIR = OUTPUT_DIR / "results"
MODEL_DIR = OUTPUT_DIR / "models"

# Cleaned dataset produced in Week 1 (src/02_data_cleaning.py in the Week 1 repository).
# The checksum confirms this copy is byte-identical to the Week 1 output.
CLEAN_DATA_PATH = PROCESSED_DIR / "telco_churn_clean.csv"
CLEAN_DATA_SHA256 = "ec3ef03fbe050a90c06893621f92720beaa3136176ef5e91e1b5fc4d40164fec"
WEEK1_REPOSITORY = "https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-1"
ORIGINAL_SOURCE = "https://github.com/IBM/telco-customer-churn-on-icp4d"

RANDOM_SEED = 42

for _directory in (PROCESSED_DIR, FIGURE_DIR, TABLE_DIR, RESULTS_DIR, MODEL_DIR):
    _directory.mkdir(parents=True, exist_ok=True)
