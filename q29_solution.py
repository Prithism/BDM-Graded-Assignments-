import csv

act_f, shift_f = "dataset_3_232.xlsx - Actual_Output.csv", "dataset_3_232.xlsx - Shift_Running.csv"
dates = ["2022-04-08", "2022-04-09", "2022-04-10", "2022-04-11", "2022-04-12", "2022-04-13", "2022-04-14"]

status = {}
with open(shift_f, newline='') as f:
    for r in csv.DictReader(f): status[r["Date"]] = [r[f"Shift {i} (8 Hours)"] for i in range(1,4)]

ops, total = 0, 0
with open(act_f, newline='') as f:
    for r in csv.DictReader(f):
        if r["Date"].split(" ")[0] in dates:
            for i in range(1,4):
                if status[r["Date"]][i-1] == "Operational":
                    ops += 1
                    total += int(r[f"Shift {i}"])

if ops > 0:
    print(round(total / (ops * 4800), 4))
