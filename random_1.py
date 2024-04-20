import pandas as pd
import numpy as np

def highest_scoring_year() :
    constructors_df = pd.read_csv('constructors.csv')
    constructor_points_df = pd.read_csv('constructor_standings.csv')

    # join on the constructorId column
    merged_df = pd.merge(constructors_df, constructor_points_df, on='constructorId')

    # Group by constructor and find the maximum points value at the end of any race for each one
    max_points_df = merged_df.groupby(['constructorId', 'name', 'nationality'])['points'].max().reset_index()

    # Rename columns for clarity
    max_points_df.columns = ['constructorId', 'teamName', 'nationality', 'highest_season_points']
    #sort constructors by max points value
    sorted = max_points_df.sort_values(by='highest_season_points', ascending=False)
    
    return sorted

