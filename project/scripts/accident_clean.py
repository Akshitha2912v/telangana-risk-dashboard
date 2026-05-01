import pandas as pd

# Load dataset
df = pd.read_csv("data_raw/accidents.csv")

# Clean column names
df.columns = df.columns.str.lower().str.strip()

# Rename columns
df = df.rename(columns={
    'state name': 'state',
    'city name': 'district'
})

# Keep only Telangana
df = df[df['state'].str.lower().str.contains('telangana')]

# Remove unknown cities
df = df[df['district'].str.lower() != 'unknown']

# Create accident count
df['accident_count'] = 1

# Group by district
df_clean = df.groupby('district')['accident_count'].sum().reset_index()

# Save cleaned file
df_clean.to_csv("data_clean/accidents_clean.csv", index=False)

print("✅ Accident data cleaned!")