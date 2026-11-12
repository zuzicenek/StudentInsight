-- StudentInsight
-- Student Retention and Academic Performance Analysis

-- 1. Distribution of student statuses

SELECT
    stav_studia,
    COUNT(*) AS pocet_studentu,
    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM students), 2
    ) AS podil_pct
FROM students
GROUP BY stav_studia
ORDER BY pocet_studentu DESC;


-- 2. Student outcomes by study programme

SELECT
    studijni_program,
    COUNT(*) AS pocet_studentu,

    SUM(CASE
        WHEN stav_studia = 'Absolvoval(a)'
        THEN 1 ELSE 0
    END) AS absolventi,

    SUM(CASE
        WHEN stav_studia = 'Ukončeno školou'
        THEN 1 ELSE 0
    END) AS ukonceni_skolou

FROM students
GROUP BY studijni_program
ORDER BY ukonceni_skolou DESC;


-- 3. School-initiated termination by faculty

SELECT
    fakulta,
    COUNT(*) AS pocet_studentu,

    SUM(CASE
        WHEN stav_studia = 'Ukončeno školou'
        THEN 1 ELSE 0
    END) AS ukonceni_skolou

FROM students
GROUP BY fakulta
ORDER BY ukonceni_skolou DESC;


-- 4. Terminations by year of study

SELECT
    rocnik,
    COUNT(*) AS pocet_studentu,

    SUM(CASE
        WHEN stav_studia = 'Ukončeno školou'
        THEN 1 ELSE 0
    END) AS ukonceni_skolou,

    SUM(CASE
        WHEN stav_studia = 'Dobrovolně ukončil(a)'
        THEN 1 ELSE 0
    END) AS dobrovolna_ukonceni

FROM students
GROUP BY rocnik
ORDER BY rocnik;


-- 5. Reasons for ending studies

SELECT
    duvod_ukonceni,
    COUNT(*) AS pocet_pripadu

FROM students

WHERE duvod_ukonceni IS NOT NULL
  AND TRIM(duvod_ukonceni) <> ''

GROUP BY duvod_ukonceni
ORDER BY pocet_pripadu DESC;


-- 6. Average credits by study status

SELECT
    stav_studia,
    ROUND(AVG(ziskane_kredity), 2)
        AS prumer_ziskanych_kreditu,

    ROUND(AVG(ocekavane_kredity), 2)
        AS prumer_ocekavanych_kreditu

FROM students
GROUP BY stav_studia;