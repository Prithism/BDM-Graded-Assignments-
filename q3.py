import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_1.csv")

df = pd.read_csv(
    CSV_PATH,
    skiprows=1
)

responded_df = df[df["RESPONSE_STATUS"] == "Accepted"]

total_households = len(responded_df)

no_two_wheeler_want_to_buy = responded_df[
    (responded_df["TWO_WHEELERS_OWNED"] == 0) &
    (responded_df["WILL_BUY_TWO_WHEELER"] == "Y")
]

count = len(no_two_wheeler_want_to_buy)

fraction = count / total_households

print(f"Total responding households                        : {total_households}")
print(f"Households with no two-wheeler & want to buy one  : {count}")
print(f"Fraction                                           : {count}/{total_households} = {fraction:.4f}")
print(f"Percentage                                         : {fraction * 100:.2f}%")
