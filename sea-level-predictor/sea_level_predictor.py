import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')

    plt.figure(figsize=(10, 6))

    # Create scatter plot
    sns.scatterplot(x='Year', y='CSIRO Adjusted Sea Level', data=df, color='blue', label='Observed Data')

    # Create first line of best fit
    lr_1880_2012 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051), 
             lr_1880_2012.slope * range(1880, 2051) + lr_1880_2012.intercept, 
             color='orange', label='Fit Line 1880-2012')

    # Create second line of best fit
    df_2000 = df.query('Year >= 2000')
    lr_2000_2012 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051), 
             lr_2000_2012.slope * range(2000, 2051) + lr_2000_2012.intercept, 
             color='green', label='Fit Line 2000-2012')

    # Add labels and title

    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()