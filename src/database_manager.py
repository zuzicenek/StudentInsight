from pathlib import Path
import sqlite3

import pandas as pd


class DatabaseManager:
    """Manages the local SQLite database."""

    def __init__(self):
        self.project_dir = Path(__file__).resolve().parent.parent

        self.database_dir = self.project_dir / "database"

        self.database_file = (
            self.database_dir / "student_insight.db"
        )

    def save_data(self, df):
        """Save cleaned student data into SQLite."""

        print("\nSaving data to SQLite...")

        self.database_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        # Convert missing pandas values to SQL NULL
        database_df = df.astype(object).where(
            pd.notna(df),
            None
        )

        with sqlite3.connect(self.database_file) as connection:

            database_df.to_sql(
                "students",
                connection,
                if_exists="replace",
                index=False
            )

            # Indexes for frequently used columns
            connection.execute("""
                CREATE INDEX IF NOT EXISTS idx_students_program
                ON students (studijni_program)
            """)

            connection.execute("""
                CREATE INDEX IF NOT EXISTS idx_students_status
                ON students (stav_studia)
            """)

        print("Database successfully created.")

    def execute_query(self, query):
        """Execute a SQL SELECT query and return a DataFrame."""

        with sqlite3.connect(self.database_file) as connection:

            result = pd.read_sql_query(
                query,
                connection
            )

        return result