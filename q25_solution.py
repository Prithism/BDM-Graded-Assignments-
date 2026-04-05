import csv

data_file = "dataset_3_232.xlsx - Data.csv"
m_map = {"April":1,"May":2,"June":3,"July":4,"August":5,"September":6,"October":7,"November":8,"December":9,"January":10,"February":11,"March":12}

rows = []
with open(data_file, newline='') as f:
    for row in csv.DictReader(f):
        rows.append(row)

rows.sort(key=lambda x: (x["Gear Assembly"], int(x["Fiscal Year"][:4]), m_map[x["Month"]]))

gear_stock = {}
period_inv = {}
for row in rows:
    gear = row["Gear Assembly"]
    gear_stock[gear] = gear_stock.get(gear, 0) + int(row["Quantity Produced"]) - int(row["Sales Quantity"])
    if row["Month"] in ["June", "September", "December", "March"]:
        key = f"{row['Quarter']}{row['Fiscal Year']}"
        period_inv[key] = sum(gear_stock.values())

if period_inv:
    print(min(period_inv, key=period_inv.get))
