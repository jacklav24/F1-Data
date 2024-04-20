import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from constructorMapping import getConstructorMapping
def getAllConstructorResults() :
    ''' this portion of the code gets the winning constructorId each year and their point value '''

    # Read the CSV files for standings and races
    constructor_standings = pd.read_csv('./data/constructor_standings.csv')
    races = pd.read_csv('./data/races.csv')

    # Merge based on race id
    merged_df = pd.merge(constructor_standings, races, on='raceId')

    # Group by 'year', 'constructorId' then find the maximum points for each group
    max_points = merged_df.groupby(['year', 'constructorId'])['points'].max().reset_index()

    ''' after this line, we have stored every single end-of-year point value for each constructor to a row. but we still have duplicate years.
        now, we sort them by ascending points... thus, when we later remove duplicates of years, we will be left with only the first occuring 
        values... that is, the point value of the winners that year.'''

    max_points.sort_values(by='points', ascending=False, inplace=True)

    return max_points


def get_column_names_excluding(df, excluded_column):
    return [col for col in df.columns if col != excluded_column]

def graphAll(frame, y_cols):
    '''Now let's create a graph!'''
    x = frame.index
    for y_col in y_cols:
        y = frame[y_col]
        plt.plot(x, y, marker='.', label=y_col)

    ax = plt.gca()
    ax.set_xlim([1958, 2024])
    ax.set_ylim([0, 800])
    plt.xticks(np.arange(min(x), max(x) + 1, 10))
    plt.yticks(np.arange(0, 800 + 50, 25.0))

    plt.legend()  # Add legend to show labels of each line
    plt.title('Your Title Here')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')

    plt.show()
    

allResults = getAllConstructorResults()



#merged = pd.merge(allResults, constructorsAndIds, on='constructorId')
pivot_df = allResults.pivot_table(index='year', columns='constructorId', values='points')
print(pivot_df.columns)
print(pivot_df.index)

pivot_df = getConstructorMapping(pivot_df)
print("hiiiii\n", pivot_df)
# Reset the index to make 'year' a column instead of the index
pivot_df.reset_index(inplace=True)

# Fill any missing values with 0 (if a player didn't score points in a certain year)
pivot_df.fillna(0, inplace=True)

# Rename the columns to include 'points_' prefix
#pivot_df.columns = ['year'] + ['name' for col in pivot_df.columns[1:]]
y_cols = get_column_names_excluding(pivot_df, 'year')
graphAll(pivot_df, y_cols)
#pivot_df = pivot_df.sort_values(by="constructorId")
