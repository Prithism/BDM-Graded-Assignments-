import pandas as pd
import os

# Build a path relative to this script's location — works on any machine
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_2.csv")

# Load the CSV, skipping the first blank row
df = pd.read_csv(CSV_PATH, skiprows=1)

# Filter for Retail loans in FY21 only
retail_fy21 = df[(df["Segment of Loan"] == "Retail") & (df["Years"] == "FY21")]

# Sum of Original Loan size given by Private Banks in FY21 Retail segment
pvt_bank_value = retail_fy21[retail_fy21["Lender Name"] == "PVT Bank"]["Original Loan size"].sum()

# Sum of Original Loan size given by PSU Banks in FY21 Retail segment
psu_bank_value = retail_fy21[retail_fy21["Lender Name"] == "PSU Bank"]["Original Loan size"].sum()

# Ratio = PVT Bank retail loan value / PSU Bank retail loan value
ratio = pvt_bank_value / psu_bank_value

print(f"PVT Bank Retail loan value (FY21)    : {pvt_bank_value:,.0f}")
print(f"PSU Bank Retail loan value (FY21)    : {psu_bank_value:,.0f}")
print(f"Ratio (PVT Bank / PSU Bank)          : {ratio:.4f}")
