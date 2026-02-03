# ai_data_quality_agent
🤖 AI Data Quality Agent

An intelligent Streamlit application designed to automatically analyze, score, and clean datasets. It supports both local file uploads (CSV/XLSX) and direct integration with Google Cloud Storage (GCS).

🚀 Features

Multi-Source Loading: Support for local CSV/Excel files and Google Cloud Storage (gs:// URIs).

Automated Data Cleaning: Options for mean/mode imputation, duplicate removal, row dropping, and IQR-based outlier removal.

Quality Scoring Dashboard: A weighted scoring system (0-100) based on Completeness, Uniqueness, Validity, Outlier Impact, and Integrity.

Visual Insights: Interactive correlation heatmaps and dataset summaries.

Smart Recommendations: Heuristic-based suggestions to improve your data quality.

📋 Prerequisites

Before running the application, ensure you have the following installed and configured:

1. Python Environment

Python 3.8+: Ensure you have a modern version of Python installed.

Virtual Environment (Recommended): Use venv or conda to manage dependencies.

2. Required Python Libraries

Install all dependencies using pip:

pip install streamlit pandas numpy matplotlib seaborn scikit-learn openpyxl google-cloud-storage


Library

Purpose

streamlit

UI framework and web server.

pandas

Data manipulation and analysis.

numpy

Numerical operations and matrix handling.

matplotlib & seaborn

Data visualization and heatmaps.

scikit-learn

Specifically SimpleImputer for handling missing values.

openpyxl

Necessary for reading .xlsx (Excel) files.

google-cloud-storage

Required for GCP/GCS integration.

3. Google Cloud Platform (GCP) Setup (Optional)

If you intend to use the GCS integration (gs:// paths), follow these steps:

GCP Project: An active Google Cloud project.

Authentication: - Locally: Install the Google Cloud SDK and run gcloud auth application-default login.

In Production: The service account running the app must have the Storage Object Viewer (roles/storage.objectViewer) permission for the target bucket.

Enable APIs: Ensure the Cloud Storage API is enabled in your GCP console.

🛠️ Installation & Usage

Clone the project or copy ai_data_quality_agent.py to your local machine.

Install dependencies:

pip install -r requirements.txt 
# Or install manually using the command in the Prerequisites section.


Run the application:

streamlit run ai_data_quality_agent.py


Access the App: Open your browser and navigate to http://localhost:8501.

📊 How the Quality Score Works

The agent calculates an Overall Quality Score based on these weighted metrics:

Completeness (40%): Measures the percentage of non-null cells.

Uniqueness (20%): Measures the ratio of unique rows to total rows.

Validity (20%): Heuristic check for consistent data types within columns.

Outlier Impact (10%): Evaluates the presence of statistical outliers using the Interquartile Range (IQR).

Integrity (10%): Analyzes the strength and consistency of relationships between numeric columns.

📝 Usage Notes

GCS URIs: Ensure the URI follows the format gs://bucket-name/folder/file.csv.

Encoding: The app automatically attempts UTF-8 and Latin-1 encodings for CSV files.

Outliers: The IQR method uses a 1.5 multiplier. Columns with zero variance are automatically skipped to prevent calculation errors.

