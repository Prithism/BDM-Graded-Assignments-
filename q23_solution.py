import csv

cost_file = "dataset_3_232.xlsx - Cost.csv"
data_file = "dataset_3_232.xlsx - Data.csv"

costs = {}
with open(cost_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        gear, fy = row["SALES DETAILS (GEAR ASSEMBLIES)"], row["FY"]
        costs[(gear, fy)] = sum(int(row[k]) for k in ["Direct Materials", "Direct Labour", "Production Overhead", "G&A Overhead", "Finance Costs"])

losses = {}
with open(data_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        gear, fy = row["Gear Assembly"], row["Fiscal Year"]
        price, qty = int(row["Price"]), int(row["Sales Quantity"])
        cost = costs.get((gear, fy), 0)
        losses[gear] = losses.get(gear, 0) + (qty * (price - cost))

if losses:
    print(min(losses, key=losses.get))
