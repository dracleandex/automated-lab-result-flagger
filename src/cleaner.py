# src/cleaner.py
import pandas as pd
import re

def clean_currency_and_text(value):
    """
    Removes text like 'mg/dL' or '(High)' from numeric cells.
    Example: '105 mg/dl' -> 105.0
    """
    if pd.isna(value):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    
    # String manipulation: extract numbers and decimals only
    clean_val = re.sub(r'[^\d.]', '', str(value))
    
    try:
        return float(clean_val)
    except ValueError:
        return None

def normalize_gender(sex):
    """
    Standardizes gender to 'male' or 'female' (lowercase).
    Handles: M, F, Male, Female, m, f
    """
    if pd.isna(sex):
        return 'unknown'
    
    sex_str = str(sex).strip().lower()
    
    if sex_str in ['m', 'male']:
        return 'male'
    elif sex_str in ['f', 'female']:
        return 'female'
    else:
        return 'unknown'

def clean_data(df):
    """
    Master cleaning function.
    """
    df_clean = df.copy()

    # 1. Clean Numeric Columns (Hemoglobin & Glucose)
    # We apply the text stripper function to these specific columns
    target_cols = ['Hemoglobin', 'Fasting_Glucose']
    for col in target_cols:
        df_clean[col] = df_clean[col].apply(clean_currency_and_text)

    # 2. Normalize Gender (Critical for reference ranges)
    df_clean['Sex'] = df_clean['Sex'].apply(normalize_gender)

    # 3. Drop rows where critical data is still missing (optional)
    # df_clean = df_clean.dropna(subset=['Hemoglobin', 'Fasting_Glucose'])

    print("✅ Data cleaning complete.")
    return df_clean