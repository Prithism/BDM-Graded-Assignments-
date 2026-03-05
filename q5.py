import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_1.csv")

df = pd.read_csv(
    CSV_PATH,
    skiprows=1
)

responded_df = df[df["RESPONSE_STATUS"] == "Accepted"]

urban_households = responded_df[responded_df["REGION_TYPE"] == "URBAN"]

total_urban = len(urban_households)

no_two_wheeler_buy_now = urban_households[
    (urban_households["TWO_WHEELERS_OWNED"] == 0) &
    (urban_households["WILL_BUY_TWO_WHEELER_NOW"] == "Y")
]

count = len(no_two_wheeler_buy_now)

fraction = count / total_urban

print(f"Total urban responding households                        : {total_urban}")
print(f"Urban households with no two-wheeler & buy immediately   : {count}")
print(f"Fraction                                                 : {count}/{total_urban} = {fraction:.4f}")
print(f"Percentage                                               : {fraction * 100:.2f}%")
