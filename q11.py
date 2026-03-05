import pandas as pd
import os

# Build a path relative to this script's location – works on any machine
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset_1_107.xlsx - Data_1.csv")

# Load the CSV (skip the first blank row that contains no headers)
df = pd.read_csv(CSV_PATH, skiprows=1)

# Keep only valid responses
responded = df[df["RESPONSE_STATUS"] == "Accepted"]

# Define Rural Farmers: REGION_TYPE == "RURAL" and OCCUPATION_GROUP contains "Farmers"
rural_farmers = responded[(responded["REGION_TYPE"] == "RURAL") & responded["OCCUPATION_GROUP"].str.contains("Farmers", na=False)]

total_rural_farmers = len(rural_farmers)

# At least one two‑wheeler owned
rural_farmers_with_two = rural_farmers[rural_farmers["TWO_WHEELERS_OWNED"] >= 1]

count = len(rural_farmers_with_two)

fraction = count / total_rural_farmers if total_rural_farmers else 0

print(f"Total Rural Farmer households          : {total_rural_farmers}")
print(f"Rural Farmer households with ≥1 two‑wheeler: {count}")
print(f"Fraction                                 : {count}/{total_rural_farmers} = {fraction:.4f}")
print(f"Percentage                               : {fraction * 100:.2f}%")
