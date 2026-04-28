import pandas as pd

df = pd.read_csv("data/cloud_costs.csv")

print("📊 Cloud Cost Data")
print(df)

print("\n💰 Total cost per service:")
print(df.groupby("service")["cost"].sum())