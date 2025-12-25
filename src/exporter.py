from src.settings import PROCESSED_DATA_DIR, OUTPUT_FILE_NAME
import os

def export_results(df):
    """
    Saves three files:
    1. Master list (Everyone).
    2. Abnormal list (Flagged).
    3. Normal list (Healthy).
    """
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    
    # 1. THE ABNORMAL (Sick)
    abnormal_df = df[df['Needs_Review'] == True]
    abnormal_path = PROCESSED_DATA_DIR / "abnormal_patients.xlsx"
    abnormal_df.to_excel(abnormal_path, index=False)
    
    # 2. THE NORMAL (Healthy)
    normal_df = df[df['Needs_Review'] == False]
    normal_path = PROCESSED_DATA_DIR / "normal_patients.xlsx"
    normal_df.to_excel(normal_path, index=False)

    # 3. THE MASTER LIST (Everyone - Cleaned)
    master_path = PROCESSED_DATA_DIR / "all_patients_master.xlsx"
    df.to_excel(master_path, index=False)
    
    # Print Summary
    print("\n" + "="*30)
    print("📊 FINAL REPORT SUMMARY")
    print("="*30)
    print(f"Total Patients:   {len(df)}")
    print(f"Abnormal Findings: {len(abnormal_df)}")
    print(f"Normal Findings:   {len(normal_df)}")
    print("-" * 20)
    print(f"📂 Files saved in: {PROCESSED_DATA_DIR}")
    print("="*30 + "\n")