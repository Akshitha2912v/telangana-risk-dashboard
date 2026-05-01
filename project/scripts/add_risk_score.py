import pandas as pd

df = pd.read_csv("data_clean/final_dataset.csv")

# Convert health risk to numeric
def health_score(x):
    if x == "High":
        return 3
    elif x == "Medium":
        return 2
    else:
        return 1

df['health_score'] = df['health_risk'].apply(health_score)

# Create total risk score
df['total_risk'] = (
    df['accident_count'] * 0.5 +
    df['health_score'] * 15 -
    df['avg_rainfall'] * 0.2
)

# Categorize risk
def risk_label(x):
    if x > 60:
        return "High"
    elif x > 40:
        return "Medium"
    else:
        return "Low"

df['risk_level'] = df['total_risk'].apply(risk_label)

df.to_csv("data_clean/final_dataset.csv", index=False)

print("✅ Risk added")