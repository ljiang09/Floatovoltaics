'''
Stores gathered data for Dry Bulb temperature and relative humidity over
time, as well as humidity ratios based on these two values.
Plots the humidity ratios over time for a span of one year.
'''

import numpy as np


# https://www.weatherwx.com/climate-averages/az/lake+mead.html
HIGH_TEMPERATURES = np.array([54, 58, 66, 75, 83, 96, 100, 98, 91, 77, 64, 52])  # degrees F
LOW_TEMPERATURES = np.array([41, 44, 51, 58, 66, 77, 83, 83, 76, 61, 50, 41])  # degrees F
WIND_SPEEDS = np.array([6, 7, 9, 10, 9, 10, 9, 8, 7, 7, 6, 6])  # mph
RELATIVE_HUMIDITIES = np.array([44, 38, 30, 22, 18, 14, 21, 22, 22, 26, 32, 43])  # percentage

# singular values for July, the hottest month.
# temp and relative humidity are gathered from data, ratio is found using psychrometric chart
DRY_BULB_TEMPERATURE = 91.5  # Fahrenheit
RELATIVE_HUMIDITY = 21  # percent
HUMIDITY_RATIO_NUM = 45  # grains per pound. this should be divided by 7000 to get the direct ratio


# unit conversions
AVERAGE_TEMPERATURES = (HIGH_TEMPERATURES + LOW_TEMPERATURES)/2
WIND_SPEEDS = WIND_SPEEDS * 0.44704
RELATIVE_HUMIDITIES = RELATIVE_HUMIDITIES / 7000

print(AVERAGE_TEMPERATURES)
print(WIND_SPEEDS)
print(RELATIVE_HUMIDITIES)
