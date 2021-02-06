import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

#plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
plt.bar(x, y, label='bars1', color='#42f554')
plt.bar(x, y, label='bar2')


plt.xlabel('x')
plt.ylabel('y')
# add subtitle with(new line charater) \n without space as below
plt.title('Interesting Graph\nCheck it out')
# for legend we use keyword argument
plt.legend()
plt.show()
