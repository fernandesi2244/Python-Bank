import pandas as pd, matplotlib.pyplot as plt
from scipy.stats import linregress

class StatsAnalysis(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.df = pd.read_csv('Bank Research Initiative/'+fileName)
    
    def regression(self, x_var, y_var):
        self.df = self.df[self.df[y_var] != 0]
        ageBalanceDf = self.df[[x_var,y_var]][:100]
        ageBalanceDf.plot(kind='scatter',x=x_var,y=y_var,color='red')
        x = ageBalanceDf.Age
        y = ageBalanceDf.EstimatedSalary
        stats = linregress(x,y)
        m = stats.slope
        b = stats.intercept
        plt.plot(x, m*x+b, color="blue")
        plt.show()
