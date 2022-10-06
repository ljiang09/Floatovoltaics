
DENSITY = 1000 # Density of water (kg/m^3)
A_max = 640000000 # m^2
V_max = 32236000000 # m^3

x_s = 0.014659 # maximum humidity ratio of saturated air at the same temperature as the water surface (kg/kg)  (kg H2O in kg Dry Air)
#! ^^ placeholder value
x = # humidity ratio air (kg/kg) (kg H2O in kg Dry Air)

V_in = 12000	# ft^3 / s
V_dam = 8000	# ft^3 / s
V_evap = cndjdnajkcl # this will be a function of surface area, which we can calculate from V/h

v_air = 10 #! placeholder value


dVdt = V_in - V_dam - V_evap


# kg / (m^2 * h)
Theta = 25+19*v_air			# v_air = velocity of air
  
# Rate of evaporation of water, g_s. Units of kg/s
A = 
V_evap = Theta*A*(x_s - x) / (3600 * DENSITY)

