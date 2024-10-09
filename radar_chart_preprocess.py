import pandas as pd

# Load your dataset
df = pd.read_csv('climate_change_impact_on_agriculture_2024.csv')

# Group by 'Year' and 'Country', then aggregate using the mean
aggregated_df = df.groupby(['Year', 'Country']).agg({
    'Soil_Health_Index': 'mean',
    'Fertilizer_Use_KG_per_HA': 'mean',
    'Pesticide_Use_KG_per_HA': 'mean',
    'Irrigation_Access_%': 'mean'
}).reset_index()

# Save the processed DataFrame to a new CSV file
aggregated_df.to_csv('agricultural_resources.csv', index=False)

print("Data has been saved to 'aggregated_data_by_year_country.csv'")