import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data = df)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line_x = list(range(min(df['Year']), 2051))
    line_y = [slope * yeari + intercept for yeari in line_x]
    plt.plot(line_x, line_y, color='red')

    # Create second line of best fit
    df2000 = df[df.Year>=2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    line_x2 = list(range(2000, 2051))
    line_y2 = [slope2 * yearj + intercept2 for yearj in line_x2]
    plt.plot(line_x2, line_y2, color='green')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()