'''
Stores gathered data for Dry Bulb temperature and relative humidity over
time, as well as humidity ratios based on these two values.
Plots the humidity ratios over time for a span of one year.
'''

import numpy as np

DRY_BULB_TEMPERATURES = [91.5]  # Fahrenheit
RELATIVE_HUMIDITIES = [21]  # percent
HUMIDITY_RATIO_NUMS = [45]  # grains per pound. this should be divided by 7000 to get the direct ratio

