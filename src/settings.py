# src/settings.py
import os
from pathlib import Path

# Get the project root directory (2 levels up from src/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Define Data Paths
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
CONFIG_DIR = BASE_DIR / "config"

# File Names
INPUT_FILE_NAME = "lab_results.xlsx"
OUTPUT_FILE_NAME = "flagged_results.xlsx"

# Expected Columns (Standardizing names)
REQUIRED_COLUMNS = ['Patient_ID', 'Age', 'Sex', 'Hemoglobin', 'Fasting_Glucose']