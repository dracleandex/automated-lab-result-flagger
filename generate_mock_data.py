import pandas as pd
import numpy as np
import random
import os

# Setup directories
os.makedirs('data/raw', exist_ok=True)

def generate_data(num_patients=50):
    data = []
    
    for i in range(num_patients):
        sex = random.choice(['Male', 'Female', 'M', 'F'])
        age = random.randint(18, 90)
        p_id = f"PAT-{1000+i}"
        
        # Simulate Hemoglobin
        if random.random() < 0.2:
            hb = round(random.uniform(7.0, 11.0), 1)
        else:
            hb = round(random.uniform(12.0, 18.0), 1)
            
        # Simulate Glucose
        if random.random() < 0.15:
            glucose = random.randint(130, 250)
        else:
            glucose = random.randint(70, 110)
            
        # Dirty Data
        if i == 5: glucose = "105 mg/dl"
        if i == 10: hb = None
            
        data.append({
            'Patient_ID': p_id, 'Age': age, 'Sex': sex,
            'Hemoglobin': hb, 'Fasting_Glucose': glucose
        })
        
    df = pd.DataFrame(data)
    df.to_excel('data/raw/lab_results.xlsx', index=False)
    print(f"✅ Generated {num_patients} patient records.")

if __name__ == "__main__":
    generate_data()