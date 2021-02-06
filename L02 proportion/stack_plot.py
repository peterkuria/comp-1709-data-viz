
"""
The idea of stack plots is to show "parts to the whole" over time. A stack plot is basically like a pie-chart, only over time.

Let's consider a situation where we have 24 hours in a day, and we'd like to see how we're spending our time. We'll divide our activities into: Sleeping, eating, working, and playing.

We're going to assume that we're tracking this over the course of 5 days, so our starting data will look like:
Here, we can see, at least in colors, how we're spending our data. The problem is, we don't really know which color is which without looking back at the code. The next problem is, with polygons, we cannot actually have "labels" for the data. So anywhere where there is more than just a line, with things like fills or stackplots like this, we cannot label the specific parts inherently. That shouldn't stop a programmer however. We can hack our way around this:
"""
import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]


plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()