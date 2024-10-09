import pandas as pd

# Load your dataset
file_path = 'climate_change_impact_on_agriculture_2024.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Group by Year, Country, and Crop_Type, then sum the Crop_Yield_MT_per_HA
df_grouped = df.groupby(['Year', 'Country', 'Crop_Type'])['Crop_Yield_MT_per_HA'].sum().reset_index()

# Save the grouped data to a new CSV file
output_file_path = 'agriculture_productivity_by_country_year.csv'  # Replace with your desired output path
df_grouped.to_csv(output_file_path, index=False)

print(f"Processed data saved to: {output_file_path}")