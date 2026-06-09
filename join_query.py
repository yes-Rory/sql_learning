import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# cursor.execute(
#     """
#     SELECT students.name,students.gender,scores.score
#     FROM students
#     INNER JOIN scores
#     ON students.student_id=scores.student_id
#     """
# )

# reserve both sides，保留两表中的所有数据，匹配不到的使用null填充
# cursor.execute(
#     """
#     SELECT *
#     FROM students
#     INNER JOIN scores
#     ON students.student_id=scores.student_id
#     """
# )

# reserve students table,保留左表中的所有数据，右表匹配不到的使用null填充
# cursor.execute(
#     """
#     SELECT *
#     FROM students
#     LEFT JOIN scores
#     ON students.student_id=scores.student_id
#     """
# )

# reserve scores table，保留右表中的所有数据，左表匹配不到的使用null填充
# cursor.execute(
#     """
#     SELECT *
#     FROM students
#     RIGHT JOIN scores
#     ON students.student_id=scores.student_id
#     """
# )

cursor.execute(
    """
   
    """
    # SELECT SUM(amount)
    # FROM orders

    # SELECT COUNT(*)
    # FROM orders

    # SELECT COUNT(DISTINCT customer_id)
    # FROM orders

    # SELECT customer_id,
    #         SUM(amount) AS total_amount
    # FROM orders
    # GROUP BY customer_id

    # SELECT DISTINCT gender
    # FROM students

    # SELECT COUNT(DISTINCT gender)
    # FROM students

    # SELECT COUNT(DISTINCT student_id)
    # FROM students

    # SELECT students.name
    # FROM students 
    # LEFT JOIN scores
    # ON students.student_id=scores.student_id
    # WHERE scores.student_id IS NULL

    # SELECT gender,COUNT(*)
    # FROM students
    # GROUP BY gender
    
    # SELECT gender,AVG(score)
    # FROM students
    # GROUP BY gender

    # SELECT gender,MAX(score)
    # FROM students
    # GROUP BY gender

    # SELECT gender,MIN(score)
    # FROM students
    # GROUP BY gender

    # SELECT gender,SUM(score)
    # FROM students
    # GROUP BY gender

    # SELECT gender,
    #        COUNT(*) AS student_count,
    #        AVG(score) AS avg_score,
    #        MAX(score) AS max_score,
    #        MIN(score) AS min_score,
    #        SUM(score) AS total_score
    # FROM students
    # GROUP BY gender

    # SELECT CASE
    #             WHEN score >=90 THEN 'A'
    #             WHEN score >=80 THEN 'B'
    #             WHEN score >=70 THEN 'C'
    #             ELSE 'D'
    #         END AS grade,
    #         COUNT(*) AS student_count,
    #         ROUND(AVG(score),2) AS avg_score
    # FROM students
    # GROUP BY grade
    # ORDER BY avg_score DESC

    # UPDATE students
    # SET score = 89
    # WHERE name='Rose'

    # DELETE FROM students
    # WHERE name="Bob"

    # SELECT *
    # FROM students
    # WHERE score < (
    #     SELECT AVG(score)
    #     FROM students
    # )

    # SELECT *
    # FROM students
    # ORDER BY score DESC
    # LIMIT 1

    # SELECT *
    # FROM students
    # WHERE score = (
    #     SELECT MAX(score)
    #     FROM students
    # )

    # SELECT *
    # FROM students
    # WHERE name IN ('Tom','Lucy','Alice')

    # SELECT *
    # FROM students
    # WHERE name NOT IN ('Tom','Lucy')

    # SELECT students.gender,
    #         AVG(score)
    # FROM students
    # INNER JOIN scores
    # ON students.student_id=scores.student_id
    # GROUP BY students.gender

    # SELECT gender,
    #         COUNT(*) AS count
    # FROM students
    # GROUP BY gender

)

result=cursor.fetchall()
# print(result)

# output data
for row in result:
    print(row)

# close database
conn.close()