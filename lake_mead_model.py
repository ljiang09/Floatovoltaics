'''
Insert docstrings here
'''

import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


def model(V, t, V_in, V_dam):
    '''
    Insert docstrings here
    '''
    DENSITY = 1000  # Density of water (kg/m^3)

    # maximum humidity ratio of saturated air at the same temperature as the water surface (kg/kg)  (kg H2O in kg Dry Air)
    MAX_HUM_RATIO = 0.014659
    HUM_RATIO = 0.01  # humidity ratio air (kg/kg) (kg H2O in kg Dry Air)
    #! ^^ placeholder values

    LENGTH = 3.18  # meters
    area = (2*V) / math.sqrt(V/LENGTH)

    v_air = 10  # ! placeholder value

    # kg / (m^2 * h)
    Theta = 25+(19*v_air)			# v_air = velocity of air

    # this will be a function of surface area, which we can calculate from V/h
    V_evap = Theta*area*(MAX_HUM_RATIO - HUM_RATIO) / (DENSITY)
    # dVdt = V_in - V_dam - V_evap
    dVdt = -V_evap
    print(dVdt)
    return dVdt


def cfsToM3Hr(cfs):
    '''
    Insert docstrings here
    '''
    return cfs * 0.028316846711688 * 3600


def m3ToKm3(m3):
    '''
    Insert docstrings here
    '''
    return m3 / (1000000000)


V_in = cfsToM3Hr(11800)  # m^3 / hr
V_dam = cfsToM3Hr(11600)  # m^3 / hr

V_0 = 10000000000  # ! Placeholder, m^3

t = np.linspace(0, 20000, 20)

result = odeint(model, V_0, t, args=(V_in, V_dam))

fig, ax = plt.subplots()
ax.plot(t, m3ToKm3(result), label='V_0 = 10km^3')
ax.legend()
ax.set_xlabel('Time (hrs)')
ax.set_ylabel('Volume (km^3)')

plt.show()
