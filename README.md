# Supply Chain Analytics: Correlation Matrix Visualization

**Author Email:** 24f2006003@ds.study.iitm.ac.in

## Project Overview
This project analyzes supplier performance data for a major automotive manufacturer.  
The goal is to identify relationships between key supply chain metrics to improve  
supplier selection, inventory planning, and cost optimization.

**Dataset Variables:**
- Supplier_Lead_Time (Days from order placement to delivery)
- Inventory_Levels (Units in stock)
- Order_Frequency (Orders per month)
- Delivery_Performance (On-time delivery rate %)
- Cost_Per_Unit (Unit cost in $)

## Process
1. **Enable Data Analysis ToolPak** in Excel.
2. Import dataset into Excel.
3. Use **Data → Data Analysis → Correlation** to create correlation matrix.
4. Copy results to a new sheet.
5. Apply **Conditional Formatting → Color Scales → Red-White-Green**.
   - Red = Low correlation
   - White = Neutral correlation
   - Green = High correlation
6. Take screenshot (400x400–512x512 px) of the heatmap.
7. Export correlation matrix as CSV.

## Files in this Repository
- **README.md** — This file, with project description and author email.
- **correlation.csv** — Exported correlation matrix from Excel.
- **heatmap.png** — Screenshot of Excel conditional formatting heatmap.

## How to View
- [View correlation.csv](./correlation.csv)
- [View heatmap.png](./heatmap.png)