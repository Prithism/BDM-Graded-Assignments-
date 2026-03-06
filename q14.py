import pandas as pd
import os

# Build a path relative to this script's location — works on any machine
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_2.csv")

# Load the CSV, skipping the first blank row
df = pd.read_csv(CSV_PATH, skiprows=1)

# Filter for Commercial loans issued by Private Banks only
pvt_commercial = df[
    (df["Segment of Loan"] == "Commercial") &
    (df["Lender Name"] == "PVT Bank")
]

# Sum of Original Loan size for PVT Bank commercial loans in FY19
fy19_value = pvt_commercial[pvt_commercial["Years"] == "FY19"]["Original Loan size"].sum()

# Sum of Original Loan size for PVT Bank commercial loans in FY20
fy20_value = pvt_commercial[pvt_commercial["Years"] == "FY20"]["Original Loan size"].sum()

# Relative growth % = ((FY20 - FY19) / FY19) * 100
# abs() gives the absolute float as required
growth_pct = abs((fy20_value - fy19_value) / fy19_value) * 100

print(f"PVT Bank Commercial loan value FY19  : {fy19_value:,.0f}")
print(f"PVT Bank Commercial loan value FY20  : {fy20_value:,.0f}")
print(f"Absolute growth % (FY19 → FY20)      : {growth_pct:.4f}%")
print(f"As absolute float                    : {growth_pct:.4f}")
