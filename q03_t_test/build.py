# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def t_statistic(df):
    
    z, p = stats.ttest_1samp(a = df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean = df['GrLivArea'].mean())

    return p , z>0.1

df.columns


