import pandas as pd
import random

# Load your final dataset
df = pd.read_csv("data_clean/final_dataset.csv")

# Generate hospital count (simulate)
random.seed(42)
df['hospitals'] = [random.randint(1, 10) for _ in range(len(df))]

# Create health risk
def health_risk(x):
    if x < 3:
        return "High"
    elif x < 6:
        return "Medium"
    else:
        return "Low"

df['health_risk'] = df['hospitals'].apply(health_risk)

# Save
df.to_csv("data_clean/final_dataset.csv", index=False)

print("✅ Health data added!")