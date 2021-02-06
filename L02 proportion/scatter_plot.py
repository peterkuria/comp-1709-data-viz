"""
Scatter plots is usu to compare two variables, 
or three if you are plotting in 3 dimensions, looking for 
correlation or groups.
The plt.scatter allows us to not only plot on x and y, but it also lets us decide on the color, size, and type of marker we use. There are a bunch of marker options, see the Matplotlib Marker Documentation for all of your choices.

"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

# (See matplotlib maker types](https://matplotlib.org/3.3.3/api/markers_api.html)
plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o", s=10)

plt.scatter(x,y, label='skitscat', color='k', s=25, marker="*")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()