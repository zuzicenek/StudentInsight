from pathlib import Path
import pandas as pd


class StudentDataProcessor:
    """Loads, cleans and validates student data."""

    def __init__(self):
        self.project_dir = Path(__file__).resolve().parent.parent
        self.excel_file = (
            self.project_dir
            / "data"
            / "student_retention_dataset.xlsx"
        )

        self.required_columns = [
            "student_id",
            "fakulta",
            "studijni_program",
            "forma_studia",
            "rok_nastupu",
            "rocnik",
            "stav_studia",
            "duvod_ukonceni",
            "akademicky_rok_ukonceni",
            "ziskane_kredity",
            "ocekavane_kredity"
        ]

        self.allowed_statuses = {
            "Aktivní",
            "Absolvoval(a)",
            "Dobrovolně ukončil(a)",
            "Ukončeno školou"
        }

    def load_data(self):
        """Load data from Excel."""

        print("\nLoading student data...")

        if not self.excel_file.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.excel_file}"
            )

        df = pd.read_excel(
            self.excel_file,
            sheet_name="students_raw"
        )

        print(f"Loaded records: {len(df)}")

        return df

    def clean_data(self, df):
        """Clean and validate the dataset."""

        print("\nCleaning student data...")

        df = df.copy()

        df.columns = df.columns.str.strip()

        # Check required columns
        missing_columns = [
            col for col in self.required_columns
            if col not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing columns: {missing_columns}"
            )

        # Remove duplicate student records
        original_count = len(df)

        df = df.drop_duplicates(
            subset=["student_id"],
            keep="first"
        )

        print(
            f"Duplicates removed: "
            f"{original_count - len(df)}"
        )

        # Clean text columns
        text_columns = [
            "student_id",
            "fakulta",
            "studijni_program",
            "forma_studia",
            "stav_studia",
            "duvod_ukonceni",
            "akademicky_rok_ukonceni"
        ]

        for column in text_columns:
            df[column] = (
                df[column]
                .astype("string")
                .str.strip()
                .replace("", pd.NA)
            )

        # Convert numeric columns
        numeric_columns = [
            "rok_nastupu",
            "rocnik",
            "ziskane_kredity",
            "ocekavane_kredity"
        ]

        for column in numeric_columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

        # Remove records without essential information
        df = df.dropna(
            subset=["student_id", "stav_studia"]
        )

        # Validate study statuses
        invalid_statuses = (
            set(df["stav_studia"].dropna())
            - self.allowed_statuses
        )

        if invalid_statuses:
            raise ValueError(
                f"Unknown study statuses: {invalid_statuses}"
            )

        # Negative credit values are invalid
        for column in [
            "ziskane_kredity",
            "ocekavane_kredity"
        ]:
            invalid_values = df[column].lt(0).fillna(False)
            df.loc[invalid_values, column] = pd.NA

        print(f"Records after cleaning: {len(df)}")

        return df