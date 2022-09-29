
V_in = 12000	# ft^3 / s
V_dam = 8000	# ft^3 / s
# V_evap = cndjdnajkcl # this will be a function of surface area, which we can calculate from V/h

dV_dt = V_in - V_dam - V_evap


# Rate of evaporation of water, g_s. Units of kg/s
Theta = 25+19*v_air			# v_air = velocity of air
# A = ncdjkncsjndk    # kg / (m^2 * h)
g_s = Theta*A*(x_s - x) / 3600

