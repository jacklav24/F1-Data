import pandas as pd
import numpy as np

df = pd.read_csv('constructors.csv')

print(df)

data2 = pd.read_csv("constructor_results.csv")

# Step 1: Read the original CSV file into a pandas DataFrame
original_df = pd.read_csv('constructors.csv')

# Step 2: Select only the columns you want to keep
columns_to_keep = ['name', 'nationality']  # Replace with the columns you want to keep
selected_columns_df = original_df[columns_to_keep]

# Step 3: Write the selected columns to a new CSV file
selected_columns_df.to_csv('constructorandNatl.csv', index=False)

#constructorsToKeep = df[]

#print(' hi ' + data2.columns)
#print(data2)
#print('whatup')
#print(result)


# Read the CSV files into pandas DataFrames
constructor_country_df = pd.read_csv('constructors.csv')
constructor_points_df = pd.read_csv('constructor_standings.csv')

# Perform a join operation on the player_id column
merged_df = pd.merge(constructor_country_df, constructor_points_df, on='constructorId')

# Group by player and find the maximum points_in_game for each player
max_points_df = merged_df.groupby(['constructorId', 'name', 'nationality'])['points'].max().reset_index()

# Rename columns for clarity
max_points_df.columns = ['constructorId', 'teamName', 'nationality', 'highest_season_points']

max_points_df.to_csv("highest_points_finish.csv", index=False)
# Display the resulting DataFrame
print(max_points_df)