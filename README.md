# Retail Intelligence & Customer Segmentation Dashboard

## Overview

This project focuses on Retail Intelligence and Customer Segmentation analysis. It includes an ETL (Extract, Transform, Load) pipeline to process raw retail data and a Power BI dashboard for visualization.

## Project Structure

- **`src/`**: Contains the source code for the ETL pipeline.
    - `etl_pipeline.py`: Script to clean and process the raw data.
- **`data/`**: Directory for data files.
    - `raw/`: Raw input data (e.g., `online_retail_II.csv`).
    - `processed/`: Processed data ready for analysis.
- **`Retail_Executive_Dashboard.pbix`**: Power BI dashboard file.
- **`requirements.txt`**: List of Python dependencies.

## Setup & Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the ETL Pipeline

To clean and process the raw data, run the `etl_pipeline.py` script:

```bash
python src/etl_pipeline.py
```

This script will:
1.  Load the raw data from `data/raw/online_retail_II.csv`.
2.  Clean the data (remove missing Customer IDs, handle cancellations, filter non-product codes).
3.  Save the processed data to `data/processed/processed_retail_data.csv`.

### Viewing the Dashboard

Open `Retail_Executive_Dashboard.pbix` with Microsoft Power BI Desktop to interact with the visual analysis.

## Data Source

The dataset used is the "Online Retail II" dataset, which contains transactions between 01/12/2009 and 09/12/2011 for a UK-based and registered non-store online retail.
