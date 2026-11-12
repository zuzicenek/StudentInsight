from pathlib import Path


class StudentAnalyzer:
    """Analyzes student data using SQL queries."""

    def __init__(self, database):
        self.database = database

        self.project_dir = Path(__file__).resolve().parent.parent
        self.output_dir = self.project_dir / "output"

        self.queries = {

            "program_summary": """
                SELECT
                    studijni_program,
                    COUNT(*) AS pocet_studentu,

                    SUM(
                        CASE
                            WHEN stav_studia = 'Absolvoval(a)'
                            THEN 1 ELSE 0
                        END
                    ) AS absolventi,

                    SUM(
                        CASE
                            WHEN stav_studia = 'Ukončeno školou'
                            THEN 1 ELSE 0
                        END
                    ) AS ukonceni_skolou,

                    ROUND(
                        100.0 * SUM(
                            CASE
                                WHEN stav_studia = 'Ukončeno školou'
                                THEN 1 ELSE 0
                            END
                        ) / COUNT(*),
                        2
                    ) AS podil_ukonceni_pct

                FROM students
                GROUP BY studijni_program
                ORDER BY podil_ukonceni_pct DESC;
            """,

            "status_summary": """
                SELECT
                    stav_studia,
                    COUNT(*) AS pocet_studentu,

                    ROUND(
                        100.0 * COUNT(*) /
                        (SELECT COUNT(*) FROM students),
                        2
                    ) AS podil_pct

                FROM students
                GROUP BY stav_studia
                ORDER BY pocet_studentu DESC;
            """,

            "faculty_summary": """
                SELECT
                    fakulta,
                    COUNT(*) AS pocet_studentu,

                    SUM(
                        CASE
                            WHEN stav_studia = 'Ukončeno školou'
                            THEN 1 ELSE 0
                        END
                    ) AS ukonceni_skolou,

                    SUM(
                        CASE
                            WHEN stav_studia = 'Dobrovolně ukončil(a)'
                            THEN 1 ELSE 0
                        END
                    ) AS dobrovolna_ukonceni

                FROM students
                GROUP BY fakulta
                ORDER BY ukonceni_skolou DESC;
            """,

            "year_summary": """
                SELECT
                    rocnik,
                    COUNT(*) AS pocet_studentu,

                    SUM(
                        CASE
                            WHEN stav_studia = 'Ukončeno školou'
                            THEN 1 ELSE 0
                        END
                    ) AS ukonceni_skolou,

                    SUM(
                        CASE
                            WHEN stav_studia = 'Dobrovolně ukončil(a)'
                            THEN 1 ELSE 0
                        END
                    ) AS dobrovolna_ukonceni

                FROM students
                GROUP BY rocnik
                ORDER BY rocnik;
            """,

            "reason_summary": """
                SELECT
                    duvod_ukonceni,
                    COUNT(*) AS pocet_pripadu

                FROM students

                WHERE duvod_ukonceni IS NOT NULL
                  AND TRIM(duvod_ukonceni) <> ''

                GROUP BY duvod_ukonceni
                ORDER BY pocet_pripadu DESC;
            """,

            "credits_summary": """
                SELECT
                    stav_studia,

                    ROUND(
                        AVG(ziskane_kredity),
                        2
                    ) AS prumer_ziskanych_kreditu,

                    ROUND(
                        AVG(ocekavane_kredity),
                        2
                    ) AS prumer_ocekavanych_kreditu

                FROM students
                GROUP BY stav_studia
                ORDER BY prumer_ziskanych_kreditu DESC;
            """
        }

    def generate_reports(self):
        """Generate and export analytical reports."""

        print("\nGenerating analytical reports...")

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        for report_name, query in self.queries.items():

            result = self.database.execute_query(query)

            output_file = (
                self.output_dir / f"{report_name}.csv"
            )

            result.to_csv(
                output_file,
                index=False,
                encoding="utf-8-sig"
            )

            print(f"\nReport created: {report_name}.csv")
            print(result.to_string(index=False))

        print("\nAll reports generated successfully.")