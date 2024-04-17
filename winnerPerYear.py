import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from graph import line_graph

# function to write a file 'name' from a dataFram df.
def write(name, df) :
    df.to_csv(name, index = False)

''' Here, we will read from 3 data sets to get the constructor's champion for each year, and their points value.
    Because of how the data is set up, it proves to be a little difficult. Or at least more than you'd think. follow along!'''
# First, read the CSV files for constructor




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

# Remove duplicate years so we're left with only the max points each year
max_points = max_points.drop_duplicates('year')

# Rename the columns


# sort the data by year. descending
max_points.sort_values(by='year', ascending=False, inplace=True)

# save the data
winners = max_points


''' now, we could be done... however, the "constructor_standings" file does not contain the constructor names. so, to see more details
    about them, we need to merge one more time.'''
# get the dataFrame of all constructors
constructors = pd.read_csv('./data/constructors.csv')

# merge with winners by id
merged = pd.merge(constructors, winners, on='constructorId')

# ignore unwanted columns and keep these
final = merged[['year', 'points', 'name', 'nationality']]

# rename them for ease of access
final.columns = ['year', 'points', 'team', 'nation']

# apply styling to points. if ends in .0, drop the decimal
final.insert(2, "points_float", final['points'].astype(float), True)
final['points'] = final['points'].apply(lambda x: str(int(x)) if x.is_integer() else "{:.1f}".format(x))
final['year'] = final['year'].astype(int)

# getting a dataframe for output ignoring the float points value.
for_printing = final[['year', 'points', 'team', 'nation']]

# create text alignment
aligned_print = for_printing.style
aligned_print.set_properties(subset=['points'], **{'text-align': 'right'})
aligned_print.set_properties(subset=['team'], **{'text-align': 'left'})
aligned_print.set_properties(subset=['nation'], **{'text-align': 'left'})

# Sort the DataFrame by 'year' column in descending order
for_printing = final.sort_values(by='year', ascending= True)

'''uncomment this to create the file once.'''
#write('result_files/constructors_championship_winners.csv', final)
# Finally, print the df without the index!
print(for_printing.to_string(index = False))


line_graph(final, 'year', 'points_float', True)
