import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd




def line_graph(frame, x_col, y_col, dots) :
    '''Now lets create a graph!'''
    frame = frame.sort_values(x_col)
    x = frame[x_col]
    y = frame[y_col]
    plt.plot(x, y, color = 'blue', ls = '-', marker = '.')

    ax = plt.gca()
    ax.set_xlim([1958, 2024])
    ax.set_ylim([0, 800])
    plt.xticks(np.arange(min(x), max(x)+1, 10))
    plt.yticks(np.arange(min(y), max(y)+50, 25.0))

    plt.show()

