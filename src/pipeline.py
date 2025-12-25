# src/pipeline.py
from src.loader import load_data
from src.validator import validate_columns
from src.cleaner import clean_data
from src.flagger import flag_records
from src.exporter import export_results

def run_pipeline():
    print("🚀 Starting Lab Result Flagger Pipeline...\n")
    
    # Step 1: Load
    df = load_data()
    
    # Step 2: Validate
    validate_columns(df)
    
    # Step 3: Clean
    df_clean = clean_data(df)
    
    # Step 4: Flag (Apply Medical Logic)
    df_flagged = flag_records(df_clean)
    
    # Step 5: Export
    export_results(df_flagged)
    
    print("✨ Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()