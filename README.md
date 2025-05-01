# Task 7: Basic Sales Summary from SQLite Database

## 📋 Objective

This project reads sales data from a small SQLite database (`sales_data.db`) and displays:
- Total quantity sold per product category
- Total revenue per product category
- A simple bar chart of revenue per subcategory

---

## 🛠 Tools Used
- Python 3
- SQLite (via `sqlite3`)
- pandas
- matplotlib

---

## 📁 Project Files
- `main.py` - Python script that processes the data and creates the chart
- `new merged_orders.sql` - SQL file containing table creation and insert data
- `sales_chart.png` - Output chart (generated after running the script)
- `README.md` - You’re reading it :)

---

## 🚀 How to Run

1. Make sure the following Python packages are installed:
   ```bash
   pip install pandas matplotlib
2.Place both main.py and new merged_orders.sql in the same directory.

3.Run the script:
  ```bash
  python main.py
```

4.The script will:
- Create a new sales_data.db database
- Load the SQL from new merged_orders.sql
- Query for sales summary
- Display the results in the terminal
- Save a bar chart as sales_chart.png
