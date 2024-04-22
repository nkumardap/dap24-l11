import pandas as pd
import matplotlib.pyplot as plt

"""
Today we will be graphing weather data for a fictional city using 
weather_data.csv. It contains the following variables:

Date: The date for each recorded weather observation. Formatted as YYYY-MM-DD.
Max Temperature: The maximum temperature recorded on a given day, measured in 
    degrees Celsius
Min Temperature: The minimum temperature recorded on a given day, measured in 
    degrees Celsius
Precipitation: The amount of precipitation recorded on a given day, measured 
    in millimeters
Wind Speed: The average wind speed recorded on a given day, measured in 
    kilometers per hour
Humidity: The average humidity percentage recorded on a given day

The data covers the period of a single year.
"""

"""
EXERCISE 1

Open the weather data, and convert the dates into a date time object. Plot the
Maximum temperature and the minimum temperature in a single plot. Give them 
different colors and linestyles.

Remember to...
- Label the lines and create a legend
- Add a title
- Label the x-axis and y-axis
- Create a title

Save the figure as 'temperature.png' with high resolution 
"""

"""
EXERCISE 2

Create a fig object with three axes, one below the other.

On the first, plot the precipitation; on the second, plot the wind speed; and 
on the third, plot the humidity.. Ensure that all three have different colors, though
you can use the same solid lines.

For each, remember to add a title and labels for the x-axis and y-axis.

Save the entire graph as weather.png

Hint: the matplotlib method tight_layout() can be used to prevent overlap 
"""