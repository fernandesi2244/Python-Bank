import pandas as pd, matplotlib.pyplot as plt
from scipy.stats import linregress

class StatsAnalysis(object):
    def __init__(self, file_name):
        self.fileName = file_name
        self.df = pd.read_csv('Bank Research Initiative/'+file_name)

    def display(self, columns, indexing_value = None, num_rows = None):
        if indexing_value is not None:
            copy = self.df
            copy.set_index(indexing_value, inplace=True)
        else:
            copy = self.df
        if num_rows is not None:
            print(copy[columns][:num_rows])
        else:
            print(copy[columns])
        print()

    def regression(self, x_var, y_var, num_points=None):
        copy = self.df[self.df[y_var] != 0]
        if num_points is not None:
            requestedDf = copy[[x_var,y_var]][:num_points]
        else:
            requestedDf = copy[[x_var,y_var]]
        requestedDf.plot(kind='scatter',x=x_var,y=y_var,color='red')

        x = requestedDf[x_var]
        y = requestedDf[y_var]
        stats = linregress(x,y)
        m = stats.slope
        b = stats.intercept
        plt.plot(x, m*x+b, color="blue")
        plt.show()
    
    def five_num_summary(self, column_name):
        df_no_zero = self.df[self.df[column_name]!=0]
        copy = df_no_zero[column_name]

        min_val = copy.min()
        q1 = copy.quantile(.25)
        median = copy.median()
        q3 = copy.quantile(.75)
        max_val = copy.max()

        print('Printing 5-Number Summary for', column_name)
        for i in range (30+len(column_name)):
            print("-", end="")
        print()
        print(f'{"Minimum:":16s}{min_val:,.2f}')
        print(f'{"First Quartile:":16s}{q1:,.2f}')
        print(f'{"Median:":16s}{median:,.2f}')
        print(f'{"Third Quartile:":16s}{q3:,.2f}')
        print(f'{"Maximum":16s}{max_val:,.2f}')
