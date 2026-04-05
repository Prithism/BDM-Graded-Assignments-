import csv

dataset = "dataset_3_232.xlsx - Data.csv"
q1_sales = {}

with open(dataset, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["GA Category"] == "BS4 Only" and row["Quarter"] == "Q1":
            gear = row["Gear Assembly"]
            q1_sales[gear] = q1_sales.get(gear, 0) + int(row["Sales Quantity"])

if q1_sales:
    print(max(q1_sales, key=q1_sales.get))
