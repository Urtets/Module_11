import pandas as pd

# print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))
# print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))
# print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
#               'Sue': ['Pretty good.', 'Bland.']},
#              index=['Product A', 'Product B']))
#
# print(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))

exchange_figures = pd.read_csv("TICKER_AFH9.csv", index_col=0)
print(exchange_figures.head())
print(help(pd.read_csv))


