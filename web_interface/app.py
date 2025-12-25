import sys
import os
from flask import Flask, render_template, request, send_from_directory
import pandas as pd

# --- PATH FIX: Allow app.py to see the 'src' folder ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
# -------------------------------------------------------

from src.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR
from src.pipeline import run_pipeline

app = Flask(__name__)

# Ensure directories exist
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

@app.route('/')
def home():
    """Renders the upload page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles file upload, runs the pipeline, and shows results."""
    # Check if the file part is present
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    
    # Check if a file was actually selected
    if file.filename == '':
        return "No file selected", 400

    # 1. Save the uploaded file
    save_path = RAW_DATA_DIR / "lab_results.xlsx"
    file.save(save_path)

    # 2. Run the processing pipeline
    print("🤖 Flask is running the analysis pipeline...")
    try:
        run_pipeline()
    except Exception as e:
        return f"❌ Error during pipeline execution: {e}", 500

    # 3. Read the output files to get counts
    abnormal_path = PROCESSED_DATA_DIR / "abnormal_patients.xlsx"
    normal_path = PROCESSED_DATA_DIR / "normal_patients.xlsx"
    
    try:
        abnormal_df = pd.read_excel(abnormal_path)
        normal_df = pd.read_excel(normal_path)
        
        abnormal_count = len(abnormal_df)
        normal_count = len(normal_df)
        total_count = abnormal_count + normal_count
        
    except Exception as e:
        return f"❌ Error reading result files: {e}", 500

    # 4. Show the result page
    return render_template('result.html', 
                           total=total_count, 
                           abnormal=abnormal_count, 
                           normal=normal_count)

@app.route('/download/<filename>')
def download_file(filename):
    """Allows the user to download the Excel files."""
    return send_from_directory(PROCESSED_DATA_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)