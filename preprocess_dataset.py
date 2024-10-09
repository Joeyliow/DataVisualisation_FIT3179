import pandas as pd

# Load the dataset
df = pd.read_csv('2023Global_GDP_By_Sector.csv')

# Step 1: Select the relevant columns
df = df[['Country/Economy', 'Total GDP (USD$)', 'Agricultural (%)', 'Agricultural (USD$)']]

# Step 2: Convert the 'Total GDP', 'Agricultural (%)', and 'Agricultural (USD$)' columns into proper numeric formats
df['Total GDP (USD$)'] = df['Total GDP (USD$)'].replace({',': ''}, regex=True).astype(float)  # Remove commas and convert to float
df['Agricultural (%)'] = df['Agricultural (%)'].str.replace('%', '').astype(float)  # Remove percentage sign and convert to float
df['Agricultural (USD$)'] = df['Agricultural (USD$)'].replace({',': ''}, regex=True).astype(float)  # Remove commas and convert to float

# Step 3: Save the cleaned dataset to a new CSV file
df.to_csv('cleaned_gdp_agriculture.csv', index=False)

# Display the first few rows of the cleaned data for review
df.head()
