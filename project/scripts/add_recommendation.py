import pandas as pd

df = pd.read_csv("data_clean/final_dataset.csv")

def recommendation(risk):
    if risk == "High":
        return "Immediate intervention needed"
    elif risk == "Medium":
        return "Monitor and improve infrastructure"
    else:
        return "Low priority - maintain conditions"

df['recommendation'] = df['risk_level'].apply(recommendation)

df.to_csv("data_clean/final_dataset.csv", index=False)

print("✅ Recommendation added")