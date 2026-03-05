import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_1.csv")

df = pd.read_csv(
    CSV_PATH,
    skiprows=1
)

responded_df = df[df["RESPONSE_STATUS"] == "Accepted"]

total_two_wheelers = responded_df["TWO_WHEELERS_OWNED"].sum()

commuter_bike_count = responded_df[
    responded_df["TYPE_OF_TWO_WHEELER_OWNED"] == "Commuter Bike"
]["TWO_WHEELERS_OWNED"].sum()

market_share = commuter_bike_count / total_two_wheelers

print(f"Total two-wheelers owned in sample   : {total_two_wheelers}")
print(f"Total Commuter Bikes owned           : {commuter_bike_count}")
print(f"Market Share of Commuter Bikes       : {commuter_bike_count}/{total_two_wheelers} = {market_share:.4f}")
print(f"Percentage                           : {market_share * 100:.2f}%")
