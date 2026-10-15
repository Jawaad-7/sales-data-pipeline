# Sales Data Pipeline

## Project Overview
A beginner friendly Data Engineering project demonstrating the ETL (Extract, Transform, Load) process. This pipeline ingests raw sales data from a CSV file, cleans it using Python and Pandas, and loads it into a SQLite database for analysis.

## Tech Stack
*   **Language:** Python
*   **Libraries:** Pandas, SQLite3
*   **Database:** SQLite

## Pipeline Steps
1.  **Ingest:** Reads `raw_sales.csv` from the data folder.
2.  **Transform:** Removes null values, formats dates, and calculates total sales.
3.  **Load:** Writes the cleaned data to a `sales.db` SQLite database.
4.  **Analyze:** Runs a SQL query to summarize total revenue by region.

## How to Run
1. Ensure you have Python installed.
2. Install Pandas: `pip install pandas`
3. Run the pipeline: `python pipeline.py`
