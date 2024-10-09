import pandas as pd

# Load the datasets
agriculture_df = pd.read_csv('Agriculture_GDP_EmploymentRate_LandSize.csv')
continent_df = pd.read_csv('continents_country.csv')

# Merge the datasets based on matching country names
merged_df = pd.merge(
    agriculture_df, 
    continent_df[['Entity', 'Continent']], 
    left_on='Country Name', 
    right_on='Entity', 
    how='left'
)

# Drop rows where any column is empty or has 0 (replace ".." with NaN for empty values)
merged_df.replace("..", pd.NA, inplace=True)
merged_df.replace(0, pd.NA, inplace=True)
cleaned_df = merged_df.dropna()

# Drop the 'Entity' column as it is redundant now
cleaned_df.drop(columns=['Entity'], inplace=True)

# Export the cleaned and modified dataset to a new CSV file
cleaned_df.to_csv('modified_Agriculture_GDP_EmploymentRate_LandSize.csv', index=False)