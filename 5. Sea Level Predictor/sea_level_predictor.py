import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = [i for i in range(df['Year'].min(), 2051)]
    y = [res.slope * i + res.intercept for i in x]
    plt.plot(x, y)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x = [i for i in range(2000, 2051)]
    y = [res.slope * i + res.intercept for i in x]
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()