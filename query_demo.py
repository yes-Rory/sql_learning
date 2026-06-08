import sqlite3

# connect database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(
    """
    SELECT 
        CASE 
            WHEN score >= 90 THEN 'A'
            WHEN score >= 80 THEN 'B'
            WHEN score >= 70 THEN 'C'
            ELSE 'D' 
        END AS grade,
        COUNT(*) AS student_count
    FROM students
    GROUP BY grade
    """
)

result = cursor.fetchall()

for row in result:
    print(row)

# close database
conn.close()

# cursor.execute(
#     """
#     SELECT COUNT(*) 
#     FROM students
#     """
# )

# cursor.execute(
#     """
#     SELECT * 
#     FROM students
#     WHERE score >= 80
#     """
# )

# cursor.execute(
#     """
#     SELECT * 
#     FROM students
#     ORDER BY score DESC
#     """
# )

# cursor.execute(
#     """
#     SELECT *
#     FROM students
#     ORDER BY score DESC
#     LIMIT 3
#     """
# )

# cursor.execute(
#     """
#     SELECT COUNT(*)
#     FROM students
#     """
# )

# cursor.execute(
#     """
#     SELECT AVG(score)
#     FROM students
#     """
# )

# cursor.execute(
#     """
#     SELECT MAX(score)
#     FROM students
#     """
# )

# cursor.execute(
#     """
#     SELECT gender,AVG(score)
#     FROM students
#     GROUP BY gender
#     """
# )

# cursor.execute(
#     """
#     SELECT gender,AVG(score)
#     FROM students
#     GROUP BY gender
#     HAVING AVG(score) > 80
#     """
# )