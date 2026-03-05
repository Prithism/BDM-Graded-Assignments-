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

# Target market = only households interested in buying a two-wheeler
interested_buyers = responded_df[responded_df["WILL_BUY_TWO_WHEELER"] == "Y"]

# Total prospective two-wheeler buyers (this is our denominator)
total_buyers = len(interested_buyers)

# Among buyers, those with 24-hour electricity supply can consider electric two-wheelers
# POWER_GROUP == "24 hours" indicates full-day electricity availability
electric_eligible = interested_buyers[interested_buyers["POWER_GROUP"] == "24 hours"]

count = len(electric_eligible)

# Target market share = eligible-for-electric / all prospective buyers
market_share = count / total_buyers

print(f"Total households interested in buying a two-wheeler  : {total_buyers}")
print(f"Among them, with 24-hr electricity (electric-ready)  : {count}")
print(f"Target market share for electric two-wheelers        : {count}/{total_buyers} = {market_share:.4f}")
print(f"Percentage                                           : {market_share * 100:.2f}%")
