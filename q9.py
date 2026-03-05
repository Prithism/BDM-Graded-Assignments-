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

# Households interested in buying a two-wheeler (WILL_BUY_TWO_WHEELER == "Y")
want_to_buy = responded_df[responded_df["WILL_BUY_TWO_WHEELER"] == "Y"]

# Total households interested in buying a two-wheeler
total_want_to_buy = len(want_to_buy)

# Among those, households that have an FD (Fixed Deposit) to pledge as security
# HAS_OUTSTANDING_SAVING_IN_FIXED_DEPOSITS == "Y" means they hold an FD
eligible_for_fd_loan = want_to_buy[
    want_to_buy["HAS_OUTSTANDING_SAVING_IN_FIXED_DEPOSITS"] == "Y"
]

count = len(eligible_for_fd_loan)

# Proportion = FD holders among two-wheeler buyers / all two-wheeler intenders
proportion = count / total_want_to_buy

print(f"Households interested in buying a two-wheeler        : {total_want_to_buy}")
print(f"Among them, households with an FD (eligible)         : {count}")
print(f"Proportion eligible for lower interest FD loan       : {count}/{total_want_to_buy} = {proportion:.4f}")
print(f"Percentage                                           : {proportion * 100:.2f}%")
