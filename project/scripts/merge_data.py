import pandas as pd

# Load datasets
rain = pd.read_csv("data_clean/rainfall_clean.csv")
acc = pd.read_csv("data_clean/accidents_clean.csv")

# Clean district names
rain['district'] = rain['district'].str.lower().str.strip()
acc['district'] = acc['district'].str.lower().str.strip()

# 🔥 IMPORTANT: keep all rainfall rows
df = pd.merge(rain, acc, on='district', how='left')

# If accident data missing → fill with 0
df['accident_count'] = df['accident_count'].fillna(0)

# Save
df.to_csv("data_clean/final_dataset.csv", index=False)

print("✅ Final dataset created (fixed)")