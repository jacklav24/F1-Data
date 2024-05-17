import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import input_validation as iv
import winner_per_year as wpy
import graph as graph
import constructors as const
import constructorMapping as cm

def get_year_range(years) :
    start = iv.get_var_from_options(int, years, "Enter a start year: ", "Must be in range: ")
    end = iv.get_var_from_options(int, years, "Enter an end year: ", "Must be in range: ")
    if start < end :
        return [start, end]
    else :
        print('Try again!')
        get_year_range(years)


def main() :
    print('hello f1!')
    print("welcome to the F1 data parser. I've pulled lots of data from Kaggle, and have added some functionality. \n"
      + "You can : \n1. See all constructors results graphed for every year in F1\n"
      + "2. See the constructors results over a certain time frame\n"
      + "3. Get selected constructors results\n"
      + "4. See the winner each year, and their points scored, in the console\n"
      + "5. Enter 5 to exit!")
    
    choice = iv.get_var_from_options(int, [1,2,3,4,5],"Enter 1, 2, 3, 4, or 5 to select your choice: ", "enter an int 1, 2, 3, 4 or 5: ")

    while (choice != 5) :
        if choice == 1 :
            const.all_teams_no_range()
        elif choice == 2 :
            year_list = [year for year in range(1958, 2024)]
            years = get_year_range(year_list)
            const.all_teams_with_range(years[0], years[1])
        elif choice == 3 :
            allResults = const.get_all_constructors_results()
            teams_list = cm.get_constructor_names(allResults)
            iv.get_string_list_from_options(teams_list, "STOP","Enter a constructor name you\'d like to see results from. (Enter STOP to stop adding teams): ", "Try again! Enter a valid team name. ")
            const.selected_teams_with_range()
        elif choice == 4 :
            wpy.get_winner_per_year()
        choice = iv.get_var_from_options(int, [1,2,3,4,5],"Enter 1, 2, 3, 4, or 5 to select your choice: ", "enter an int 1, 2, 3, 4 or 5: ")
    print("thanks for looking!")
        
    
    
main()   



    