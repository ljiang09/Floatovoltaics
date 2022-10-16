'''
Insert docstrings here
'''

import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

result = []
# In descending order for legend order
panel_areas = [640000000, 600000000, 500000000, 100000000, 10000000, 1000000, 100000, 0] # m^2

MAX_AREA = 640000000  # m^2
MAX_VOLUME = 32.24 * 1000000000  # m^3
MAX_HEIGHT = 100  # meters
LENGTH = 10000 # meters
MAX_BASE = 64000 # meters
ANGLE = 89.82 # degrees

def model(V, t, V_in, V_dam):
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
    # dVdt = V_evap
    # print(V_evap/V_in)
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


V_in = cfsToM3s(11800)  # m^3 / s
V_dam = cfsToM3s(10083.3102)  # m^3 / s

# initial condition; lake mead's volume at t = 0
V_0 = MAX_VOLUME  # m^3

# represent the model time as seconds in a year
t = np.linspace(0, 31536000*10)

fig, ax = plt.subplots()

for i, panel_area in enumerate(panel_areas):
    result.append(odeint(model, V_0, t, args=(V_in, V_dam)))
    ax.plot(t/86400, m3ToKm3(result[i]), label=f'Panel Area = {panel_area} '+r'$m^2$')

ax.set_title('Volume of Lake Mead Over 10 Years')
ax.legend()
ax.set_xlabel('Time (days)')
ax.set_ylabel('Volume (km^3)')

plt.show()