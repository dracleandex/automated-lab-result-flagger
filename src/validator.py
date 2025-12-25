# src/validator.py
from src.settings import REQUIRED_COLUMNS
import sys

def validate_columns(df):
    """
    Checks if the uploaded dataframe has all required columns.
    """
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    
    if missing_cols:
        print(f"❌ Validation Failed. Missing columns: {missing_cols}")
        print(f"   Expected: {REQUIRED_COLUMNS}")
        sys.exit(1)
    
    # Check for empty dataframe
    if df.empty:
        print("❌ Validation Failed. The file is empty.")
        sys.exit(1)

    print("✅ Column validation passed.")
    return True