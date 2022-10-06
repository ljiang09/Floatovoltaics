# Question
How does the cost-effectiveness of floatovoltaics vs shade balls compare?


# General notes
97% of Lake Mead's water comes from the Colorado River, typically. It was not worth it to try to consider the other 3 percent.
Because the Diamond Creek is quite close to Lake Mead, we used the flow rate for that area in our calculations.

Outflow:

Abstract the overall shape of the lake to be a frustum.

Consider temperature of the lake as well

Height of water changes surface area which changes evaporation rate


## Relating evaporation rate to volume:
https://www.engineeringtoolbox.com/evaporation-water-surface-d_690.html

g_h = Θ(x_s - x)A

Where:

g_h = amount of evaporated water per hour (kg/h)

Θ = (25 + 19 v) = evaporation coefficient (kg/m2h)

v = velocity of air above the water surface (m/s)

A = water surface area (m^2)

x_s = maximum humidity ratio of saturated air at the same temperature as the water surface (kg/kg)  (kg H2O in kg Dry Air)

x = humidity ratio air (kg/kg) (kg H2O in kg Dry Air)

This gives us mass per hour of evaporation, but we want volume per hour because thats the thing we're using for ODEs. Thus, we divide the entire equation by density of water.

V_h = Θ(x_s - x)A / density

### We don't know the surface area yet, because it is an equation based on height of water. We need to abstract the shape of the lake to make it easier to perform calculations with, and from there come up with our own equation.

Brooke is doing this rn


### We also don't know x_s and x, since none of us are super famiilar with the concept of humidity.

Lily is working on this rn

Humidity ratio is the mass of water vapor in the air / the mass of dry air. According to the table in https://www.engineeringtoolbox.com/humidity-ratio-air-d_686.html, it is based on the temperature of the air.

https://www.watertemperature.net/united-states/lake-mead-water-temperature.html gives us the range of air temperatures of Lake Mead, which is 9.6 - 35.4 °C. For the first iteration, we will simplify this to just one number, which will be the average of these two values: 22.5 °C.

The plot in the Engineering Toolbox displays the maximum humidity ratio *x_s*. for 22.5 °C. Unfortunately there is no equation for this listed, so I'm just approximating the ratio based on the graph. This comes out to be **0.017**.

Now we need to find the value for *x*, which is the regular humidity ratio air. This value should vary day by day, even hour by hour. This means that like the surface area of the water, we will need to represent this as an equation (albeit an abstracted one). I couldn't find data for this, so I just used relative humidity measurements and calculated the ratio from there.

A simple google search did not yield any results for the humidity ratio of Lake Mead. There are several ways to find it:
* calculating it from relative humidity (which is volume-based, not mass-based like we want). Not sure if it's possible but can certainly try
* try and find data for either the masses of water vapor and dry air
* try and find data for partial pressure of water vapor in moist air and atmospheric pressure of moist air
* use a psychrometric table/chart

Resources to look at:

https://pubs.usgs.gov/of/2021/1022/ofr20211022.pdf has a plot on page 29 (39 in the pdf) for mean monthly vapor pressure
difference. But we still need the exact values in addition to this difference.

http://www.atmo.arizona.edu/students/courselinks/spring08/atmo336s1/courses/fall13/atmo551a/Site/ATMO_451a_551a_files/WaterVapor.pdf
Apparently you need to find partial pressure of water vapor in moist air. The equation on page 1 tells you how to calculate that value based on other values.

https://www.engineeringtoolbox.com/docs/documents/816/psychrometric_chart_29inHg.pdf is the psychrometric chart in high res. Why are grains a unit now :0


I ended up using the psychrometric chart (per emily's suggestion, thank you emily) to find the relationship between relative humidity, which I can easily google, and air temperature, which I can also easily google. I got 3 points for each month to get a nice spread of datapoints across the year, and for each point, I found the approximate value of the humidity ratio. This will then be converted into a ratio vs. time (days) plot. **In future iterations, it would be good to have more datapoints across multiple years to generate a more accurate model**.





Some things to note for future iterations:
* the moisture holding capacity of air increases dramatically with temperature https://www.engineeringtoolbox.com/moisture-holding-capacity-air-d_281.html. So the humidity ratio equations may be inaccurate at higher temperatures.
* 



# Action items
make a stock and flow diagram
- make a baseline lake model without solar panels (do this together)
Rain -> streams/rivers -> lake mead -> evaporation and dam outflow

create a system of equations to solve lake volume and height as a function fo time

possibly bring in the shade balls as part of the model


# Resources
Put useful websites or libraries in here!

https://plotly.com - a plotting library (?) that bill fan claims is way better than matplot lib

https://www.nps.gov/lake/learn/monitoring-the-river.htm - Colorado river stats. Bottom of page has nice links to charts

??? - rate of evaporation formula
