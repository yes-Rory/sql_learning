import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS sales")

cursor.execute(
    """
    CREATE TABLE orders(
        order_id INTEGER,
        customer_id INTEGER,
        amount INTEGER
    )
""")

cursor.execute(
    """
    CREATE TABLE sales(
        customer_id INTEGER,
        city TEXT,
        amount INTEGER
    )
""")

# insert data
cursor.executemany(
    "INSERT INTO orders VALUES(?,?,?)",
    [
        (1001,1,200),
        (1002,1,300),
        (1003,2,500),
        (1004,3,100),
        (1005,2,400),
        (1006,4,500)
    ]
)

cursor.executemany(
    "INSERT INTO sales VALUES(?,?,?)",
    [
        (1,"Shenzhen",500),
        (2,"Shenzhen",900),
        (3,"Guangzhou",100),
        (4,"Guangzhou",500),
        (5,"Shenzhen",300)
    ]
)

# commit database
conn.commit()
# close database
conn.close()