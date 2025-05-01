import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and execute SQL script
with open(r"c:\Users\Ishan\Desktop\ASSIGN\ELEVATE LABS\Task 7\new merged_orders.sql", "r") as f:
    sql_script = f.read()


# Create or connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Orders")
conn.commit()


# Execute SQL script to build tables and insert data
cursor.executescript(sql_script)
conn.commit()

# Step 2: Query to get total quantity and revenue per SubCategory
query = """
SELECT 
    SubCategory AS product,
    SUM(Quantity) AS total_qty,
    SUM(Amount) AS revenue
FROM Orders
GROUP BY SubCategory
"""
df = pd.read_sql_query(query, conn)

# Step 3: Display results
print("Sales Summary:")
print(df)

# Step 4: Bar chart of revenue per product
df.plot(kind='bar', x='product', y='revenue', title='Revenue per Product SubCategory', legend=False)
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()


