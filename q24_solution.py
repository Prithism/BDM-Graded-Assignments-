import csv

cost_file = "dataset_3_232.xlsx - Cost.csv"
data_file = "dataset_3_232.xlsx - Data.csv"

costs = {}
with open(cost_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        gear, fy = row["SALES DETAILS (GEAR ASSEMBLIES)"], row["FY"]
        costs[(gear, fy)] = sum(int(row[k]) for k in ["Direct Materials", "Direct Labour", "Production Overhead", "G&A Overhead", "Finance Costs"])

margins = {}
with open(data_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        gear, fy = row["Gear Assembly"], row["Fiscal Year"]
        price, cost = int(row["Price"]), costs.get((gear, fy), 0)
        pct = ((price - cost) / price) * 100
        if gear not in margins: margins[gear] = []
        margins[gear].append(pct)

avg_margins = {g: sum(p)/len(p) for g, p in margins.items()}
if avg_margins:
    print(max(avg_margins, key=avg_margins.get))
