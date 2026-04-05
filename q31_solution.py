import csv

act_f, shift_f = "dataset_3_232.xlsx - Actual_Output.csv", "dataset_3_232.xlsx - Shift_Running.csv"
status = {}

with open(shift_f, newline='') as f:
    for r in csv.DictReader(f): status[r["Date"]] = [r[f"Shift {i} (8 Hours)"] for i in range(1,4)]

data = {1: [], 2: [], 3: []}
with open(act_f, newline='') as f:
    for r in csv.DictReader(f):
        for i in range(1,4):
            if status[r["Date"]][i-1] == "Operational":
                data[i].append(int(r[f"Shift {i}"]))

mapes = {}
for i, outs in data.items():
    if outs:
        mean = sum(outs) / len(outs)
        mapes[f"Shift {i}"] = (sum(abs(x - mean) / mean for x in outs) / len(outs)) * 100

if mapes:
    print(max(mapes, key=mapes.get))
