import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import constructorMapping as cm



def get_all_constructors_results() :
    ''' this portion of the code gets the winning constructorId each year and their point value '''

    # Read the CSV files for standings and races
    constructor_standings = pd.read_csv('./data/constructor_standings.csv')
    races = pd.read_csv('./data/races.csv')

    # Merge based on race id
    merged_frame = pd.merge(constructor_standings, races, on='raceId')

    # Group by 'year', 'constructorId' then find the maximum points for each group
    max_points = merged_frame.groupby(['year', 'constructorId'])['points'].max().reset_index()

    ''' now we can sort by points!'''

    max_points.sort_values(by='points', ascending=False, inplace=True)

    return max_points


def get_column_names_excluding(frame, excluded_column):
    return [col for col in frame.columns if col != excluded_column]


def graph_data(frame, y_cols, beg_year, end_year):

    plt.style.use('ggplot')
    '''Now let's create a graph!'''
    start = frame.index.get_loc(beg_year)
    end = frame.index.get_loc(end_year)
    range = end - start
    max_y = 0
    plotted = []
    x = frame.index[start:end+1]
    

    for y_col in y_cols:
        
        y = frame[y_col][start:end+1]  # Slicing the y-values within the specified range
        
        if not np.isnan(y).all():  # Check if any y-value is NaN within the range
            
            plt.plot(x, y, label=y_col)
            max_y = max(max_y, y.max())  # Update maximum y-value
            plotted.append(y_col)  # Add label to list of plotted labels
        

    ax = plt.gca()
    ax.set_xlim([beg_year, end_year+1])  # Setting x-axis limits based on the specified range
    ax.set_ylim([0, max_y])  # Setting y-axis limits as before
    
    tick = range // 6
    if range // 6 < 1 : tick = 1

    
    plt.xticks(np.arange(beg_year, end_year + 1, tick))
    plt.yticks(np.arange(0, max_y + 50, 25.0))

   
    plt.legend(plotted)
    plt.title('Constructor Points Finishes')
    plt.xlabel('Years')
    plt.ylabel('Points')
    #plt.autoscale()
    

    plt.show()
    
def selected_teams_with_range(list, frame, beg_year, end_year) :
    result = frame[list]
    print(result)
    all_teams_no_range(result)

    

def all_teams_with_range(frame, beg_year, end_year) :

    allResults = get_all_constructors_results()

    #this rotates allResults so that the column names are the constructorIds, and the rows are the results each year
    pivoted_results = allResults.pivot_table(index='year', columns='constructorId', values='points')
    #now, we switch the constructor id's with the names.
    pivoted_results = cm.get_constructor_mapping(pivoted_results)
    #get the column names
    y_cols = pivoted_results.columns
    #graph all of the results from the specified years
    graph_data(pivoted_results, y_cols, beg_year, end_year)
    #pivot_df = pivot_df.sort_values(by="constructorId")

def all_teams_no_range(frame) :
    all_teams_with_range(frame, 1958, 2023)
