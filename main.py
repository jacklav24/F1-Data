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
      + "3. See the winner each year, and their points scored, in the console\n")
    
    choice = iv.get_var_from_options(int, [1,2,3,4],"Enter 1, 2, or 3 to select your choice: ", "enter an int 1, 2, or 3: ")

    if choice == 1 :
        const.no_range()
    elif choice == 2 :
        year_list = [year for year in range(1958, 2023)]
        years = get_year_range(year_list)
       
        const.with_range(years[0],years[1])
    elif choice == 3 :
        print('not yet!')
    else :
        wpy.get_winner_per_year()
        
    print()
    print('your results have been printed!')

        
    
    
main()   



    