# test_phase2.py
from src.loader import load_data
from src.validator import validate_columns
from src.cleaner import clean_data

# 1. Load
df = load_data()

# 2. Validate
validate_columns(df)

# 3. Clean
df_clean = clean_data(df)

# 4. Inspect
print("\n--- RAW VS CLEANED (First 5 Rows) ---")
print(df_clean.head())
print("\n--- Check for Cleaned Gender ---")
print(df_clean['Sex'].value_counts())