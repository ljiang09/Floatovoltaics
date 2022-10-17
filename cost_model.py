'''
Insert docstrings here
'''

import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
from lake_mead_model import model

result = []
# In descending order for legend order
panel_areas = [600000000, 400000000, 200000000, 100000000, 50000000, 25000000, 10000000, 1000000, 100000, 0] # m^2
overall_costs = []

MAX_AREA = 640 * 1000000  # m^2
MAX_VOLUME = 32 * 1000000000  # m^3
MAX_HEIGHT = 100  # m
LENGTH = 10000 # meters
MAX_BASE = 64000 # meters
ANGLE = 89.82 # degrees


PANEL_COST = 75  # dollar cost per square meter
WATER_COST = 4.45  # dollar cost per cubic meter of water
ELECTRICITY_COST = 0.127871428571  # dollar price of electricity per kWh
PANEL_KWATTS_PER_SECOND = 0.000257941667  # kWh/s for one square meter of panel
STARTING_VOLUME = 32 * 1000000000  # starting volume of lake mead. m^3


# model the saved costs over time
def costs(V, t, V_in, V_dam, panel_area):
    '''
    Insert docstrings here
    '''
    DENSITY = 1000  # Density of water (kg/m^3)

    # maximum humidity ratio of saturated air at the same temperature as the water surface (kg/kg)  (kg H2O in kg Dry Air)
    MAX_HUM_RATIO = 0.030
    HUM_RATIO = 0.015  # humidity ratio air (kg/kg) (kg H2O in kg Dry Air)

    area = 2*V / math.sqrt(V/(LENGTH*math.tan(math.radians(ANGLE))))

    v_air = 7  # m/s

    # kg / (m^2 * h)
    Theta = 25+(19*v_air)			# v_air = velocity of air

    # this will be a function of surface area, which we can calculate from V/h
    V_evap = Theta*(area-panel_area)*(MAX_HUM_RATIO - HUM_RATIO) / (DENSITY * 3600)

    dVdt = V_in - V_dam - V_evap

    return dVdt


def cfsToM3s(cfs):
    '''
    Converts cubic feet per second to meters cubed per hour.
    '''
    return cfs * 0.028316846711688


def m3ToKm3(m3):
    '''
    Convert meters cubed to km cubed.
    '''
    return m3 / (1000000000)


times = [86400*100, 86400*365, 86400*365*2, 86400*365*5, 86400*2550, 86400*365*10]  # seconds

V_in = cfsToM3s(11800)  # m^3 / s
V_dam = cfsToM3s(10083.3102)  # m^3 / s
V_0 = MAX_VOLUME  # m^3


# print(odeint(model, V_0, np.linspace(0, times[0]), args=(V_in, V_dam))[-1][0])
# print(odeint(model, V_0, np.linspace(0, times[-1]), args=(V_in, V_dam))[-1][0])
# sweep the panel areas, and the specified amounts of time
plt.figure(1)
for time in times:
    cost_values = []
    for panel_area in panel_areas:
        t = np.linspace(0, time)
        volume = odeint(costs, V_0, t, args=(V_in, V_dam, panel_area))[-1][0]
        panel_electricity_price = PANEL_KWATTS_PER_SECOND*ELECTRICITY_COST*panel_area  # total dollar price of electricity for 1 second
        cost = panel_electricity_price - panel_area*PANEL_COST + volume*WATER_COST
        cost_values.append(cost)
    plt.plot(panel_areas, cost_values, label = f'{time/86400} days')


plt.legend()
plt.title('Overall monetary value of Lake Mead after various\namounts of time of having solar panels')
plt.xlabel('Panel Size (' + r'$m^2$' + ')')
plt.ylabel('Revenue (USD)')

plt.show()
