# Automated Inventory Reorder Alert

A Python script that reads inventory data, calculates how many days of stock remain for each item, flags items that need reordering, and produces a formatted Excel report and chart.

## What it does
- Calculates **days of stock** from stock on hand and average sales
- Computes a **reorder point** using supplier lead time plus a safety buffer
- Labels each item **OUT OF STOCK**, **CRITICAL**, **REORDER**, or **OK**
- Suggests an **order quantity** to cover 4 weeks of sales
- Exports a color-coded Excel report (Action Needed, All Items, By Category) and a status chart

## How to run
```
pip install pandas openpyxl matplotlib
python generate_sample_data.py   # creates fake inventory.csv
python reorder_alert.py          # creates the Excel report and chart
```

To use your own data, replace `inventory.csv` with columns:
`item_id, item_name, category, stock_on_hand, avg_weekly_sales, lead_time_days`.

## Automating it
Run it on a schedule, e.g. every morning:
- Windows: Task Scheduler running `python reorder_alert.py`
- Mac/Linux: a cron job such as `0 7 * * * python /path/to/reorder_alert.py`

## Tools
Python, pandas, openpyxl, matplotlib

*All data is randomly generated sample data.*
