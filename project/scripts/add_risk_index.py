import pandas as pd

df = pd.read_csv("data_clean/final_dataset.csv")

# Normalize total_risk to 0–100
min_val = df['total_risk'].min()
max_val = df['total_risk'].max()

df['risk_index'] = ((df['total_risk'] - min_val) / (max_val - min_val)) * 100

# Save
df.to_csv("data_clean/final_dataset.csv", index=False)

print("✅ Risk index added")

# Show top 5 risky districts
top5 = df.sort_values(by='risk_index', ascending=False).head(5)

print("\n🔥 Top 5 High Risk Districts:")
print(top5[['district', 'risk_index']])