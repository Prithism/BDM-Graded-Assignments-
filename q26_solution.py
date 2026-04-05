import csv

data_file = "dataset_3_232.xlsx - Data.csv"
revs = {}

with open(data_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        gear, fy = row["Gear Assembly"], row["Fiscal Year"]
        revs[(gear, fy)] = revs.get((gear, fy), 0) + (int(row["Sales Quantity"]) * int(row["Price"]))

jumps = {}
for gear in set(k[0] for k in revs.keys()):
    r19, r20 = revs.get((gear, "2019-20"), 0), revs.get((gear, "2020-21"), 0)
    if r19 > 0: jumps[gear] = ((r20 - r19) / r19) * 100

if jumps:
    print(max(jumps, key=jumps.get))
