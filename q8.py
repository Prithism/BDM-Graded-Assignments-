import pandas as pd
import os

# Build a path relative to this script's location — works on any machine
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_1.csv")

df = pd.read_csv(
    CSV_PATH,
    skiprows=1
)

# Keep only valid survey responses
responded_df = df[df["RESPONSE_STATUS"] == "Accepted"]

# Total number of responding households
total_households = len(responded_df)

# Households with NO outstanding borrowing are eligible for a new loan
# HAS_OUTSTANDING_BORROWING == "N" means no existing loan
eligible_households = responded_df[responded_df["HAS_OUTSTANDING_BORROWING"] == "N"]

count = len(eligible_households)

# Proportion = eligible households / total responding households
proportion = count / total_households

print(f"Total responding households          : {total_households}")
print(f"Households with no outstanding loan  : {count}")
print(f"Proportion eligible for new loan     : {count}/{total_households} = {proportion:.4f}")
print(f"Percentage                           : {proportion * 100:.2f}%")
