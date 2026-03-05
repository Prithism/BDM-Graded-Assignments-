import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_1.csv")

df = pd.read_csv(
    CSV_PATH,
    skiprows=1
)

responded_df = df[df["RESPONSE_STATUS"] == "Accepted"]

total_households = len(responded_df)

already_have_want_more = responded_df[
    (responded_df["TWO_WHEELERS_OWNED"] >= 1) &
    (responded_df["WILL_BUY_TWO_WHEELER"] == "Y")
]

count = len(already_have_want_more)

proportion = count / total_households

print(f"Total responding households                              : {total_households}")
print(f"Households with two-wheeler & want to buy another        : {count}")
print(f"Proportion                                               : {count}/{total_households} = {proportion:.4f}")
print(f"Percentage                                               : {proportion * 100:.2f}%")
