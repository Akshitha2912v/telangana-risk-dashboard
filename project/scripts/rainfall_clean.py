import pandas as pd

# Load dataset
df = pd.read_csv("data_raw/rainfall.csv")

# Clean column names
df.columns = df.columns.str.lower().str.strip()

# Filter only Telangana data
df = df[df['state'].str.lower().str.contains('telangana')]

# Identify daily columns (all columns after state, district, month)
daily_cols = df.columns[3:]

# Convert values to numeric
df[daily_cols] = df[daily_cols].apply(pd.to_numeric, errors='coerce')

# Calculate average rainfall
df['avg_rainfall'] = df[daily_cols].mean(axis=1)

# Keep only required columns
df_clean = df[['district', 'avg_rainfall']]

# Group by district
df_clean = df_clean.groupby('district').mean().reset_index()

# Save cleaned file
df_clean.to_csv("data_clean/rainfall_clean.csv", index=False)

print("✅ Rainfall cleaned successfully!")