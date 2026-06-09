import sqlite3
# print(sqlite3.sqlite_version)

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# RANK允许并列，会跳号
# DENSE_RANK允许并列，不会跳号
cursor.execute(
    """
    SELECT *
    FROM(
        SELECT *,
        ROW_NUMBER() OVER(
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rank_num
        FROM salary
    )
    WHERE rank_num=1
    """
)
# SELECT 
#         *,
#         ROW_NUMBER() OVER(
#             PARTITION BY city
#             ORDER BY amount DESC
#         ) AS rank_num
#     FROM sales

# PARTITION BY city
# ORDER BY amount DESC

# PRRTITION BY user_id
# ORDER BY login_time DESC

# PARTITION BY month
# ORDER BY sales DESC

# PARTITON BY customer_id
# ORDER BY order_time DESC

result = cursor.fetchall()
for row in result:
    print(row)

# close database
conn.close()

#  SELECT *,
#         DENSE_RANK() OVER(
#               ORDER BY total_amount DESC
#         ) AS rank_num
# FROM (
#     SELECT customer_id,
#             SUM(amount) AS total_amount
#     FROM orders
#     GROUP BY customer_id
# )

# ROW_NUMBER()强制编号，不考虑并列
    # SELECT 
    #     customer_id,
    #     SUM(amount) AS total_amount,
    #     ROW_NUMBER() OVER(
    #         ORDER BY SUM(amount) DESC
    #     ) AS rank_num
    # FROM orders
    # GROUP BY customer_id
#  SELECT 
#         customer_id,
#         SUM(amount) AS total_amount
#     FROM orders
#     GROUP BY customer_id
#     ORDER BY total_amount DESC
#     LIMIT 1
#    SELECT 
#         SUM(amount) *1.0 / 
#         COUNT(DISTINCT customer_id) 
#         AS avg_customer_value
#     FROM orders
#   SELECT customer_id,
#             AVG(amount) AS avg_amount
#     FROM orders
#     GROUP BY customer_id
# SELECT customer_id,
#             SUM(amount) AS total_amount
#     FROM orders
#     GROUP BY customer_id

    # SELECT SUM(amount) AS total_amount,
    # COUNT(DISTINCT customer_id) 
    # FROM orders
