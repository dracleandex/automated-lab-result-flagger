import pandas as pd
import yaml
from src.settings import CONFIG_DIR

def load_reference_ranges():
    """Loads the YAML configuration file."""
    config_path = CONFIG_DIR / "reference_ranges.yaml"
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def get_range(test_config, sex):
    """
    Selects the correct low/high range based on patient sex.
    Falls back to 'default' if sex is unknown.
    """
    if sex in test_config['ranges']:
        return test_config['ranges'][sex]
    return test_config['ranges']['default']

def evaluate_test(value, ref_range):
    """Returns 'Low', 'High', or 'Normal'."""
    if pd.isna(value):
        return "Missing"
    
    if value < ref_range['low']:
        return "Low"
    elif value > ref_range['high']:
        return "High"
    return "Normal"

def flag_records(df):
    """
    Main function to process the dataframe and flag abnormalities.
    """
    config = load_reference_ranges()
    df_flagged = df.copy()
    
    # We will track if a patient needs attention
    df_flagged['Needs_Review'] = False
    
    # Iterate through rows (Standard Python logic, easier to read than complex vectorization)
    for index, row in df_flagged.iterrows():
        sex = row['Sex']
        
        # --- Check Hemoglobin ---
        hb_range = get_range(config['hemoglobin'], sex)
        hb_status = evaluate_test(row['Hemoglobin'], hb_range)
        df_flagged.at[index, 'Hb_Flag'] = hb_status
        
        # --- Check Glucose ---
        # Glucose is usually not sex-dependent, so we use 'default'
        gluc_range = config['fasting_glucose']['ranges']['default']
        gluc_status = evaluate_test(row['Fasting_Glucose'], gluc_range)
        df_flagged.at[index, 'Glucose_Flag'] = gluc_status
        
        # Mark for review if ANY test is abnormal
        if hb_status in ['Low', 'High'] or gluc_status in ['Low', 'High']:
            df_flagged.at[index, 'Needs_Review'] = True

    print("✅ medical rules applied. Abnormalities flagged.")
    return df_flagged