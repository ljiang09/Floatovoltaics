'''
Insert docstrings here
'''

import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

result = []
# In descending order for legend order
panel_areas = [600000000, 100000000, 50000000, 25000000, 10000000, 1000000, 100000] # m^2
change_in_costs = []

MAX_AREA = 640 * 1000000  # m^2
MAX_VOLUME = 32 * 1000000000  # m^3
MAX_HEIGHT = 100  # m
# LENGTH = math.sqrt(2*MAX_AREA*MAX_VOLUME/MAX_HEIGHT)  # meters
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

    panel_price = panel_area*PANEL_COST

    panel_electricity_price = PANEL_KWATTS_PER_SECOND*ELECTRICITY_COST*panel_area  # total dollar price of electricity for 1 second

    # revenue = panel_electricity_price - panel_price - water_loss_cost

    dCdt = panel_electricity_price + dVdt*WATER_COST

    change_in_costs.append(dCdt[0])

    # print(dCdt)
    return dVdt
    # print(dVdt)
    # print(dCdt)


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



def sweep_costs():
    panel_areas = [100000000, 50000000, 25000000, 10000000, 1000000, 100000, 0] # m^2
    for panel_area in panel_areas:
        costs(panel_area)


V_in = cfsToM3s(11800)  # m^3 / s
V_dam = cfsToM3s(10083.3102)  # m^3 / s

# initial condition; lake mead's volume at t = 0
V_0 = MAX_VOLUME  # m^3

# represent the model time as seconds in 10 years
t = np.linspace(0, 31536000*10, num = 59)


# for i, panel_area in enumerate(panel_areas):
#     result.append(odeint(costs, V_0, t, args=(V_in, V_dam, panel_area)))
#     ax.plot(t/86400, m3ToKm3(result[i]), label=f'Panel Area = {panel_area} '+r'$m^2$')

plt.figure(1)
plt.plot(t/86400, m3ToKm3(odeint(costs, V_0, t, args=(V_in, V_dam, panel_areas[0]))), label=f'Panel Area = {panel_areas[0]} '+r'$m^2$')
plt.title('piss')
plt.xlabel('Time (days)')
plt.ylabel('Volume '+r'($km^3$)')

print(len(t))

plt.figure(2)
plt.plot(t/86400, change_in_costs)
plt.title('shit')
plt.xlabel('Time (days)')
plt.ylabel('Cost ($)')

# odeint(costs, V_0, t, args=(V_in, V_dam, panel_areas[0]))
# plt.plot(t/86400, change_in_costs)

# ax.set_title(f'Volume of Lake Mead With Solar Panels of area {panel_areas[0]} Over 10 Years')
# ax.legend()
# ax.set_xlabel('Time (days)')
# ax.set_ylabel('Volume (km^3)')

plt.show()





# lost water = max volume - current lake volume
# ^ multiply this by the water cost

# For each water volume over 1 second:
# - Panel cost + price of solar panel electricity production - cost of water lost



# Look into conversion factors for how much lost water is worth to us. How much solar generation 

# [3.2e+10]
# [3.20014184e+10]
# [3.20014184e+10]
# [3.20028367e+10]
# [3.20028367e+10]
# [3.21677504e+10]
# [3.21677509e+10]
# [3.2332255e+10]
# [3.2332256e+10]
# [3.24963532e+10]
# [3.24963542e+10]
# [3.30623921e+10]
# [3.30623968e+10]
# [3.36236574e+10]
# [3.36236511e+10]
# [3.35034054e+10]
# [3.3503402e+10]
# [3.39414946e+10]
# [3.39414946e+10]
# [3.4376713e+10]
# [3.43767126e+10]
# [3.48090933e+10]
# [3.48090929e+10]
# [3.56654855e+10]
# [3.56654837e+10]
# [3.65109434e+10]
# [3.65109447e+10]
# [3.73457387e+10]
# [3.73457401e+10]
# [3.81701217e+10]
# [3.8170122e+10]
# [3.89843312e+10]
# [3.89843315e+10]
# [4.05000099e+10]
# [4.05000118e+10]
# [4.19814627e+10]
# [4.19814628e+10]
# [4.34300516e+10]
# [4.34300476e+10]
# [4.48470313e+10]
# [4.48470303e+10]
# [4.6233588e+10]
# [4.62335874e+10]
# [4.7590818e+10]
# [4.75908175e+10]
# [4.95011813e+10]
# [4.950118e+10]
# [5.13553827e+10]
# [5.13553819e+10]
# [5.31560503e+10]
# [5.31560535e+10]
# [5.4905615e+10]
# [5.49056164e+10]
# [5.66063079e+10]
# [5.66063083e+10]
# [5.82602037e+10]
# [5.8260204e+10]
# [5.98692331e+10]
# [5.98692333e+10]
# [6.23312291e+10]
# [6.23312301e+10]
# [6.46916416e+10]
# [6.46916449e+10]
# [6.69564251e+10]
# [6.69564279e+10]
# [6.9130987e+10]
# [6.91309891e+10]
# [7.12202688e+10]
# [7.12202702e+10]
# [7.32288031e+10]
# [7.32288042e+10]
# [7.51607631e+10]
# [7.51607639e+10]
# [7.76936314e+10]
# [7.76936332e+10]
# [8.00986967e+10]
# [8.00987013e+10]
# [8.23842053e+10]
# [8.23842084e+10]
# [8.45576456e+10]
# [8.4557648e+10]
# [8.66258596e+10]
# [8.66258613e+10]
# [8.85951163e+10]
# [8.85951175e+10]
# [9.04711794e+10]
# [9.04711803e+10]
# [9.28980713e+10]
# [9.28980735e+10]
# [9.51726386e+10]
# [9.51726443e+10]
# [9.73061136e+10]
# [9.73061175e+10]
# [9.93086582e+10]
# [9.93086613e+10]
# [1.01189517e+11]
# [1.01189519e+11]
# [1.02957119e+11]
# [1.02957121e+11]
# [1.04619176e+11]
# [1.04619177e+11]
# [1.06701574e+11]
# [1.06701577e+11]
# [1.08621199e+11]
# [1.08621205e+11]
# [1.10392063e+11]
# [1.10392067e+11]
# [1.12026752e+11]
# [1.12026755e+11]
# [1.13536624e+11]
# [1.13536626e+11]
# [1.14931949e+11]
# [1.14931951e+11]
# [1.1622204e+11]
# [1.16222041e+11]
# [1.17782566e+11]
# [1.1778257e+11]
# [1.1919097e+11]
# [1.19190978e+11]
# [1.20462863e+11]
# [1.20462869e+11]
# [1.21612092e+11]
# [1.21612097e+11]
# [1.22650988e+11]
# [1.22650991e+11]
# [1.23590546e+11]
# [1.23590548e+11]
# [1.24440591e+11]
# [1.24440593e+11]
# [1.25427852e+11]
# [1.25427856e+11]
# [1.26295247e+11]
# [1.26295255e+11]
# [1.27057678e+11]
# [1.27057684e+11]
# [1.277281e+11]
# [1.27728105e+11]
# [1.28317819e+11]
# [1.28317822e+11]
# [1.28836701e+11]
# [1.28836704e+11]
# [1.29293375e+11]
# [1.29293378e+11]
# [1.29806324e+11]
# [1.29806329e+11]
# [1.3024108e+11]
# [1.30241085e+11]
# [1.30609677e+11]
# [1.30609668e+11]
# [1.30922232e+11]
# [1.30922225e+11]
# [1.31187327e+11]
# [1.31187324e+11]
# [1.3141221e+11]
# [1.31412208e+11]
# [1.31603005e+11]
# [1.31603005e+11]
# [1.31764902e+11]
# [1.31764901e+11]
# [1.31928299e+11]
# [1.31928298e+11]





# [3.2e+10]
# [3.19997602e+10]
# [3.19997602e+10]
# [3.19995205e+10]
# [3.19995205e+10]
# [3.17454704e+10]
# [3.17454699e+10]
# [3.14928119e+10]
# [3.14928109e+10]
# [3.12415422e+10]
# [3.12415411e+10]
# [3.02915558e+10]
# [3.02915489e+10]
# [3.05207549e+10]
# [3.0520751e+10]
# [2.98115697e+10]
# [2.9811573e+10]
# [2.91139551e+10]
# [2.91139547e+10]
# [2.84278425e+10]
# [2.84278421e+10]
# [2.70899142e+10]
# [2.7089912e+10]
# [2.57973281e+10]
# [2.57973288e+10]
# [2.45496195e+10]
# [2.45496203e+10]
# [2.33462963e+10]
# [2.3346296e+10]
# [2.21868467e+10]
# [2.21868464e+10]
# [1.85799385e+10]
# [1.85799223e+10]
# [1.95580617e+10]
# [1.95580568e+10]
# [1.71752681e+10]
# [1.71752631e+10]
# [1.50296213e+10]
# [1.50296297e+10]
# [1.55180242e+10]
# [1.55180278e+10]
# [1.39944855e+10]
# [1.3994484e+10]
# [1.26000752e+10]
# [1.26000766e+10]
# [1.13299306e+10]
# [1.13299318e+10]
# [1.0178847e+10]
# [1.01788488e+10]
# [9.14129449e+09]
# [9.14129705e+09]
# [8.21141819e+09]
# [8.21142154e+09]
# [8.21141818e+09]
# [8.2114218e+09]
# [8.94690059e+09]
# [8.94690063e+09]
# [8.75676405e+09]
# [8.756764e+09]
# [8.57083817e+09]
# [8.57083819e+09]
# [8.38907386e+09]
# [8.38907386e+09]
# [8.21142122e+09]
# [8.21142122e+09]
# [7.8682494e+09]
# [7.86824944e+09]
# [7.5409152e+09]
# [7.54091533e+09]
# [7.22900436e+09]
# [7.22900452e+09]
# [6.93209611e+09]
# [6.9320963e+09]
# [6.64976386e+09]
# [6.64976407e+09]
# [6.25375052e+09]
# [6.25375128e+09]
# [5.88791428e+09]
# [5.88791465e+09]
# [5.55077365e+09]
# [5.55077318e+09]
# [5.24083403e+09]
# [5.24083422e+09]
# [4.95660014e+09]
# [4.95660034e+09]
# [4.69657652e+09]
# [4.69657668e+09]
# [4.41255431e+09]
# [4.41255451e+09]
# [4.15913343e+09]
# [4.15913361e+09]
# [3.93378918e+09]
# [3.93378904e+09]
# [3.73407399e+09]
# [3.73407358e+09]
# [3.55763617e+09]
# [3.5576355e+09]
# [3.40223522e+09]
# [3.40223432e+09]
# [3.26575488e+09]
# [3.26575381e+09]
# [3.28869625e+09]
# [3.28869568e+09]
# [3.18684326e+09]
# [3.18684304e+09]
# [3.09563133e+09]
# [3.0956309e+09]
# [3.01407983e+09]
# [3.01407948e+09]
# [2.94127559e+09]
# [2.94127525e+09]
# [2.87637105e+09]
# [2.87637073e+09]
# [2.80668772e+09]
# [2.80668722e+09]
# [2.7463241e+09]
# [2.74632401e+09]
# [2.69411577e+09]
# [2.69411659e+09]
# [2.6490259e+09]
# [2.64902624e+09]
# [2.61013111e+09]
# [2.61013128e+09]
# [2.57661718e+09]
# [2.57661734e+09]
# [2.54776781e+09]
# [2.5477679e+09]
# [2.50993221e+09]
# [2.50993275e+09]
# [2.48022116e+09]
# [2.48022354e+09]
# [2.48870165e+09]
# [2.48870236e+09]
# [2.470743e+09]
# [2.47074304e+09]
# [2.45555953e+09]
# [2.45556012e+09]