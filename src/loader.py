# src/loader.py
import pandas as pd
import sys
from src.settings import RAW_DATA_DIR, INPUT_FILE_NAME

def load_data(filename=INPUT_FILE_NAME):
    """
    Loads the raw Excel file into a pandas DataFrame.
    """
    file_path = RAW_DATA_DIR / filename
    
    try:
        print(f"📂 Loading data from: {file_path}")
        # Read Excel, treating "NA" or empty strings as NaN
        df = pd.read_excel(file_path, na_values=['NA', 'Missing'])
        print(f"✅ Loaded {len(df)} rows successfully.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        sys.exit(1)