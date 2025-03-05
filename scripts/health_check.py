import pandas as pd

data = "digEds_cat.csv"
source_df = pd.read_csv(
    "https://raw.githubusercontent.com/dig-Eds-cat/qod/refs/heads/main/result.csv"
)
target_df = pd.read_csv(data)
target_df.loc[
    target_df["URL"].isin(source_df[source_df["status"] == 200]["URL"]), "Current availability"
] = "yes"

target_df.to_csv(data, index=False)
