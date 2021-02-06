import matplotlib.pyplot as plt

"""
#######################
# PART ONE            #
#######################
import csv

x = []
y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        # convert loaded data from string into float or int
        # in this case our data is all int, plot line by line, separated by a comma
        x.append(int(row[0])) 
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

"""

import numpy as np

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

"""
The result should be the same graph. Later on, we can utilize NumPy to do some more work for us when we load the data in, but that is content for a future tutorial! Just like with the csv module not needing a .csv specifically, the loadtxt function does not require the file to be a .txt file, it could be a .csv, and it can even be a python list object!
"""