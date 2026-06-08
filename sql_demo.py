import sqlite3

# create database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# 建表前：清空表
cursor.execute(
    """
    DROP TABLE IF EXISTS students
    """
)

# donnot repeat create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    name TEXT,
    gender TEXT,
    score INTEGER
               )
""")

students = [
    ("Tom","M",90),
    ("Jack","M",85),
    ("Lucy","F",95),
    ("Rose","F",89),
    ("Mike","M",78),
    ("Alice", "F", 92),
    ("Bob", "M", 55),
    ("Emma", "F", 88),
    ("David", "M", 73),
    ("Sophia", "F", 81)
]

cursor.executemany(
    "INSERT INTO students VALUES(?,?,?)",
    students
)

# cursor.execute("""
# INSERT INTO students VALUES
# ('Jack','M',85)
# """)
# cursor.execute(
#     """
# INSERT INTO students
# VALUES('Lucy','F',95)
# """
# )
# cursor.execute(
#     """
# INSERT INTO students
# VALUES('Tom','M',90)
# """
# )
# cursor.execute("""
# INSERT INTO students VALUES
# ('Rose','F',66)
# """)
# cursor.execute("""
# INSERT INTO students VALUES
# ('Mike','M',78)
# """)
# cursor.execute("""
# INSERT INTO students VALUES
# ('Alice','F',92)
# """)
# cursor.execute("""
# INSERT INTO students VALUES
# ('Bob','M',55)
# """)
# cursor.execute("""
# INSERT INTO students VALUES
# ('Emma','F',88)
# """)
# cursor.execute("""
# INSERT INTO students VALUES
# ('David','M',73)
# """)
# cursor.execute("""
# INSERT INTO students VALUES
# ('Sophia','F',81)
# """)

# commit database
conn.commit()

# close database
conn.close()