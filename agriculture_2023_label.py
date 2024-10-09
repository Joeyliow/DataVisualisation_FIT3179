import pandas as pd

# Load your dataset
file_path = 'climate_change_impact_on_agriculture_2024.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter the dataset to only include data for the year 2023
df_2023 = df[df['Year'] == 2023]

# Group by Crop_Type and sum the Crop_Yield_MT_per_HA
df_grouped_2023 = df_2023.groupby('Crop_Type')['Crop_Yield_MT_per_HA'].sum().reset_index()

# Define the custom order for the Crop_Type, starting with Wheat
crop_order = ['Wheat', 'Vegetables', 'Soybeans', 'Corn', 'Sugarcane', 'Barley', 'Fruits', 'Coffee', 'Cotton', 'Rice']

# Ensure the dataframe follows this specific order
df_grouped_2023['Crop_Type'] = pd.Categorical(df_grouped_2023['Crop_Type'], categories=crop_order, ordered=True)

# Sort by the custom Crop_Type order
df_grouped_2023 = df_grouped_2023.sort_values('Crop_Type')

# Calculate the cumulative sum for Crop_Yield_MT_per_HA across Crop_Type for the year 2023
df_grouped_2023['Cumulative_Yield'] = df_grouped_2023['Crop_Yield_MT_per_HA'].cumsum()

# Add the 'Year' column back, as it's fixed at 2023
df_grouped_2023['Year'] = 2023

# Save the cumulative data to a new CSV file
output_file_path = 'crop_yield_labels_2023.csv'  # Replace with your desired output path
df_grouped_2023.to_csv(output_file_path, index=False)

print(f"Cumulative data for 2023 with correct order and Year saved to: {output_file_path}")