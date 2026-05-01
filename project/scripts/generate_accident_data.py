import pandas as pd
import random

# Load rainfall districts
df = pd.read_csv("data_clean/rainfall_clean.csv")

# Generate accident data
df['accident_count'] = [random.randint(10, 100) for _ in range(len(df))]

# Save as accident dataset
df[['district', 'accident_count']].to_csv("data_clean/accidents_clean.csv", index=False)

print("✅ Accident data generated!")