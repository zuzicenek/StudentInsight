from data_processor import StudentDataProcessor
from database_manager import DatabaseManager
from analyzer import StudentAnalyzer


class StudentInsightApp:

    def run(self):
        processor = StudentDataProcessor()
        database = DatabaseManager()
        analyzer = StudentAnalyzer(database)

        data = processor.load_data()
        cleaned_data = processor.clean_data(data)

        database.save_data(cleaned_data)

        analyzer.generate_reports()


if __name__ == "__main__":
    app = StudentInsightApp()
    app.run()