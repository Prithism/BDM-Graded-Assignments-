import csv

actual_f, scrap_f = "dataset_3_232.xlsx - Actual_Output.csv", "dataset_3_232.xlsx - Scrap.csv"
dates = ["2022-04-01", "2022-04-02", "2022-04-03", "2022-04-04", "2022-04-05", "2022-04-06", "2022-04-07"]

good = 0
with open(actual_f, newline='') as f1, open(scrap_f, newline='') as f2:
    r1, r2 = list(csv.DictReader(f1)), list(csv.DictReader(f2))
    for i in range(len(r1)):
        d = r1[i]["Date"].split(" ")[0]
        if d in dates:
            good += sum(int(r1[i][f"Shift {j}"]) for j in range(1,4)) - sum(int(r2[i][f"Shift {j}"]) for j in range(1,4))

print(round(good / (21 * 4800), 4))
