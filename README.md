Automated Lab Result Flagger



A lightweight HealthTech application that processes raw Excel laboratory data, applies gender-stratified clinical reference ranges, and automatically flags patients requiring medical review.



Built with \*\*Python\*\*, \*\*Flask\*\*, and \*\*Pandas\*\*.



---



\## 🏥 Problem Statement

In high-volume hospital settings, clinicians often receive lab results in massive Excel spreadsheets. Manually scanning hundreds of rows to identify abnormal values (e.g., Anemia, Hyperglycemia) is slow and prone to human error.



\## ✅ Solution

This tool automates the triage process by:

1\.  \*\*Ingesting\*\* raw Excel/CSV lab reports.

2\.  \*\*Cleaning\*\* "dirty" data (removing text from numeric fields, standardizing gender formats).

3\.  \*\*Analyzing\*\* results against configurable clinical reference ranges (sensitive to patient sex).

4\.  \*\*Sorting\*\* patients into "Abnormal" (Sick) and "Normal" (Healthy) cohorts.

5\.  \*\*Delivering\*\* results via a simple web interface.



---



\## ⚙️ Key Features

\* \*\*Web Interface (UI):\*\* Simple drag-and-drop upload via a Flask web server.

\* \*\*Gender-Specific Logic:\*\* Differentiates Reference Ranges for Males vs. Females (e.g., Hemoglobin thresholds).

\* \*\*Data Cleaning:\*\* Automatically strips units (e.g., "12.5 g/dL" → 12.5) and handles missing values.

\* \*\*Automated Reporting:\*\* Generates three distinct output files:

&nbsp;   \* `abnormal\_patients.xlsx`: Only patients needing attention.

&nbsp;   \* `normal\_patients.xlsx`: Patients within healthy ranges.

&nbsp;   \* `all\_patients\_master.xlsx`: The full cleaned dataset.



---



\## 🛠️ Tech Stack

\* \*\*Language:\*\* Python 3.x

\* \*\*Data Processing:\*\* Pandas, NumPy

\* \*\*Web Framework:\*\* Flask

\* \*\*Configuration:\*\* YAML (for easy editing of medical reference ranges)

\* \*\*File Handling:\*\* OpenPyXL



---



\## 🚀 How to Run



\### 1. Installation

Clone the repository and install dependencies:

```bash

pip install pandas flask openpyxl pyyaml

2\. Run the Application

Start the local web server:



Bash



python web\_interface/app.py

3\. Use the Tool

Open your browser to http://127.0.0.1:5000



Upload a raw lab Excel file (Example provided in data/raw/).



View the summary dashboard and download your reports.



📂 Project Structure

Plaintext



automated-lab-result-flagger/

│

├── config/

│   └── reference\_ranges.yaml    # ⚙️ Editable medical rules

│

├── src/                         # 🧠 Core Logic

│   ├── cleaner.py               # Data standardization

│   ├── flagger.py               # Clinical logic engine

│   ├── validator.py             # File integrity checks

│   └── pipeline.py              # Orchestrator

│

├── web\_interface/               # 🌐 Frontend

│   ├── app.py                   # Flask Server

│   └── templates/               # HTML UI

│

└── data/                        # 📁 Input/Output storage

🩺 Clinical Logic (Configuration)

Reference ranges are defined in config/reference\_ranges.yaml and can be updated without changing code.



Example Logic:



Hemoglobin (Male): Low < 13.5, High > 17.5 g/dL



Hemoglobin (Female): Low < 12.0, High > 15.5 g/dL



Fasting Glucose: Normal 70-100 mg/dL (Diabetes screening)



🔮 Future Improvements

HIPAA Compliance: Add data anonymization (hashing Patient IDs) before export.



Critical Alerts: Highlight life-threatening values (e.g., Hb < 7.0) in Red.



Email Integration: Automatically email the "Abnormal" report to the on-call doctor.



Author: Olayemi Daniel



Medical Student \& HealthTech Developer

