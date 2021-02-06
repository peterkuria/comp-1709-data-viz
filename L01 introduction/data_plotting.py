import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://tinyurl.com/ChrisCoDV/Products/DailySales.csv', index_col=0)
data.index = pd.to_datetime(data.index)
print(data.head())

data.plot.box(label='Box label')
plt.xlabel('Product name')
plt.ylabel('No. of products sold')
plt.title('ChrisCo sales\ndaily sales')

plt.show()
data.plot.density()
plt.xlabel('sales range')

plt.show()
data.plot.line()

plt.legend()
plt.show()
