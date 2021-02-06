# aving a title to the graph, labels on the axis, and a legend that explains what each line

import matplotlib.pyplot as plt
import pandas as pd


"""
With plt.xlabel and plt.ylabel, we can assign labels to 
those respective axis. Next, we can assign the plot's 
title with plt.title, and then we can invoke the default 
legend with plt.legend(). 
"""
# ploting two lines
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

# plt.plot(x,y) # without labels

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
# plt.show()
# add labels before show()
plt.xlabel('Plot Number')
plt.ylabel('Important var')
# add subtitle with(new line charater) \n without space as below
plt.title('Interesting Graph\nCheck it out')
# for legend we use keyword argument
plt.legend()
plt.show()



