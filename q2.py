import pandas as pd
import os

# Build a path relative to this script's location — works on any machine
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_1.csv")

# Load the CSV file (skip the first blank/junk row)
df = pd.read_csv(
    CSV_PATH,
    skiprows=1   # row 0 is blank; row 1 has the actual headers
)

# Keep only households that gave a valid response
responded_df = df[df["RESPONSE_STATUS"] == "Accepted"]

# Total number of sample households that responded
total_households = len(responded_df)

# Households with exactly ONE two-wheeler
one_two_wheeler_df = responded_df[responded_df["TWO_WHEELERS_OWNED"] == 1]
count_one_two_wheeler = len(one_two_wheeler_df)

# Fraction
fraction = count_one_two_wheeler / total_households

print(f"Total responding households        : {total_households}")
print(f"Households with exactly 1 two-wheeler: {count_one_two_wheeler}")
print(f"Fraction                           : {count_one_two_wheeler}/{total_households} = {fraction:.4f}")
print(f"Percentage                         : {fraction * 100:.2f}%")
