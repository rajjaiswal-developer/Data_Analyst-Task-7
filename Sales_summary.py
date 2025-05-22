import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")

# 1. Sales summary per product
query1 = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    ROUND(SUM(quantity * "Price(Rs.)"), 2) AS revenue 
FROM sales 
GROUP BY product;
"""
df = pd.read_sql_query(query1, conn)
print("Sales Summary per product:\n", df)


# Plot revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False, ylabel='Revenue (Rs.)', title='Revenue by Product')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()


# 2. Overall sales summary
query2 = """
SELECT 
    SUM(quantity) AS total_qty, 
    ROUND(SUM(quantity * "Price(Rs.)"), 2) AS total_revenue 
FROM sales;
"""
df_overall = pd.read_sql_query(query2, conn)
print("\nOverall Sales Summary:\n", df_overall)


# 3. Top 5 products by revenue 
query3 = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    ROUND(SUM(quantity * "Price(Rs.)"), 2) AS revenue 
FROM sales 
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;
"""
df_top5 = pd.read_sql_query(query3, conn)
print("\nTop 5 Products by Revenue:\n", df_top5)

conn.close()
