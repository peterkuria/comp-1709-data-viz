import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def graph_data(stock):

    # from a data API
    # examples of daset APIs are Quandl, google, yahoo finance, Kaggle
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)