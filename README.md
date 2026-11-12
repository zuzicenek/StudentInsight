# StudentInsight
### Student Retention & Academic Performance Analysis

StudentInsight is a data analytics portfolio project focused on student retention, academic performance and study outcomes.

The project demonstrates an end-to-end data processing workflow using Python, pandas, SQLite and SQL.

## Project Objectives

- Import student data from Excel.
- Clean and validate the dataset using Python and pandas.
- Store processed data in a relational SQLite database.
- Analyze student outcomes using SQL queries.
- Generate analytical reports in CSV format.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Application logic |
| pandas | Data processing and transformation |
| SQLite | Relational database |
| SQL | Data analysis and aggregation |
| openpyxl | Excel file processing |
| Git | Version control |

## Project Structure

```text
StudentInsight/
├── data/
│   └── student_retention_dataset.xlsx
├── database/
├── output/
├── src/
│   ├── main.py
│   ├── data_processor.py
│   ├── database_manager.py
│   └── analyzer.py
├── sql/
│   └── analysis.sql
├── requirements.txt
├── README.md
└── .gitignore
```

## Analytical Areas

The project explores:

- Distribution of student study statuses.
- Student outcomes by study programme.
- School-initiated study terminations by faculty.
- Terminations by year of study.
- Reasons for ending studies.
- Average earned credits by study status.

## Dataset

The project includes 600 synthetically generated student records.

The dataset contains:
- Study programme and faculty.
- Form and year of study.
- Study status.
- Reasons for ending studies.
- Earned and expected credits.

**Data disclaimer:** All records are artificially generated for educational and portfolio purposes. They do not represent real students or official university statistics.

## Installation and Usage

### Requirements

- Python 3.10 or newer
- pip

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd StudentInsight
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python src/main.py
```

The application automatically creates:
- A local SQLite database.
- Analytical CSV reports.

## Database and SQL

The processed dataset is stored in a local SQLite database.

Additional SQL queries are available in `sql/analysis.sql`.

The queries can be executed using an SQLite-compatible database tool after the application has created the database.

## Output

Generated reports are saved in the `output/` directory.

The local SQLite database is stored in `database/`.

Both are generated automatically when the application runs.

## Limitations

This project uses synthetic data and is intended as a demonstration of data processing and SQL analysis.

It is not a predictive model and does not establish causal relationships between study characteristics and student outcomes.

## Author

StudentInsight – Data Analytics Portfolio Project.