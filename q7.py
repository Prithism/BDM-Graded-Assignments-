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

# Filter for female-majority/dominant/only-female households using GENDER_GROUP
female_households = responded_df[
    responded_df["GENDER_GROUP"].isin(["Female Majority", "Female Dominated", "Only Female"])
]

total_female = len(female_households)

# Among female households, find those that own a Scooter
female_with_scooter = female_households[
    female_households["TYPE_OF_TWO_WHEELER_OWNED"] == "Scooter"
]

count = len(female_with_scooter)

# Proportion = scooter-owning female households / all female households
proportion = count / total_female

print(f"Total female-majority/dominant households     : {total_female}")
print(f"Female households that own a Scooter          : {count}")
print(f"Proportion                                    : {count}/{total_female} = {proportion:.4f}")
print(f"Percentage                                    : {proportion * 100:.2f}%")
