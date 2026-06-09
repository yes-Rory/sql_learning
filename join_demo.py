import sqlite3

# create database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# create table
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS scores")

# students
cursor.execute(
    """
    CREATE TABLE students(
    student_id INTEGER,
    name TEXT,
    gender TEXT
    )
    """
)
# scores
cursor.execute(
    """
    CREATE TABLE scores(
    student_id INTEGER,
    score INTEGER
    )
    """
)

# INSERT students
cursor.executemany(
    "INSERT INTO students VALUES(?,?,?)",
    [
        (1,"Tom","M"),
        (2,"Lucy","F"),
        (3, "Jack", "M"),
        (4, "Alice", "F")
    ]
)

# INSERT scores
cursor.executemany(
    "INSERT INTO scores VALUES(?,?)",
    [
        (1, 90),
        (2, 95),
        (3, 85)
    ]
)
# commit database
conn.commit()
# close database
conn.close()