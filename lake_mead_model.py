'''
Insert docstrings here
'''

import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

result = []
panel_areas = [10000, 100000, 1000000] # m^2


def model(V, t, V_in, V_dam):
    '''
    Insert docstrings here
    '''
    DENSITY = 1000  # Density of water (kg/m^3)

    # maximum humidity ratio of saturated air at the same temperature as the water surface (kg/kg)  (kg H2O in kg Dry Air)
    MAX_HUM_RATIO = 0.030
    HUM_RATIO = 0.015  # humidity ratio air (kg/kg) (kg H2O in kg Dry Air)
    #! ^^ placeholder values

    LENGTH = 3.18  # meters
    area = (2*V) / math.sqrt(V/LENGTH)

    v_air = 10  # m/s

    # kg / (m^2 * h)
    Theta = 25+(19*v_air)			# v_air = velocity of air

    # this will be a function of surface area, which we can calculate from V/h
    V_evap = Theta*(area-panel_area)*(MAX_HUM_RATIO - HUM_RATIO) / (DENSITY * 3600)
    
    dVdt = V_in - V_dam - V_evap
    # dVdt = V_evap
    print(V_evap/V_in)
    return dVdt


def cfsToM3s(cfs):
    '''
    Converts cubic feet per second to meters cubed per hour.


    '''
    return cfs * 0.028316846711688


def m3ToKm3(m3):
    '''
    Convers meters cubed per hour to cubic feet per second.

    '''
    return m3 / (1000000000)


V_in = cfsToM3s(11800)  # m^3 / s
V_dam = cfsToM3s(9800)  # m^3 / s

V_0 = 10000000000  # ! Placeholder, m^3

t = np.linspace(0, 31536000)

fig, ax = plt.subplots()

for i, panel_area in panel_areas:

    result[i] = odeint(model, V_0, t, args=(V_in, V_dam))
    ax.plot(t/86400, m3ToKm3(result), label=f'Panel Area = {panel_area}m^2')

ax.legend()
ax.set_xlabel('Time (days)')
ax.set_ylabel('Volume (km^3)')

plt.show()
