# Data_Analyst-Task-7
# 🧾 Basic Sales Summary Using SQLite and Python

## Objective

Analyze basic sales data using SQL inside Python, and display results using print statements and a bar chart.

---

## Tools & Technologies

- SQLite (via Python’s built-in `sqlite3`)
- Python Libraries: `sqlite3`, `pandas`, `matplotlib`
- Environment: Python script (`.py` file)

---

## Project Files
basic-sales-summary/
├── sales_summary.py # Python script
├── sales_data.db # SQLite database
├── sales_chart.png # Bar chart image
├── output_screenshot.png # Terminal output (screenshot)
└── README.md # Project description

---

## Dataset Details

- **Database:** `sales_data.db`
- **Table:** `sales`
- **Columns:** `id`, `product`, `quantity`, `"Price(Rs.)"`
- **Records:** 28 rows of product sales data

---

## Task Summary

- Created a SQLite database and inserted sample product data
- Executed SQL queries inside Python using `sqlite3`
- Loaded results into `pandas` for display
- Created a bar chart using `matplotlib`
- Saved chart as `sales_chart.png`

---

## SQL Queries Executed

- Total quantity and revenue per product  
- Overall total quantity and revenue  
- Top 5 products by revenue
