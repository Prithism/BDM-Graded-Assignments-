import csv

actual_f, scrap_f = "dataset_3_232.xlsx - Actual_Output.csv", "dataset_3_232.xlsx - Scrap.csv"
act, scr = 0, 0

with open(actual_f, newline='') as f:
    for row in csv.DictReader(f):
        act += sum(int(row[f"Shift {i}"]) for i in range(1,4))

with open(scrap_f, newline='') as f:
    for row in csv.DictReader(f):
        scr += sum(int(row[f"Shift {i}"]) for i in range(1,4))

if act > 0:
    print(round((act - scr) / act, 4))
