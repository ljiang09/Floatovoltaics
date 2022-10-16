# Question
How cost-effective is it to use solar panels to simultaneously prevent evaporation of Lake Mead and generate more electricity?


# General notes
97% of Lake Mead's water comes from the Colorado River, typically. It was not worth it to try to consider the other 3 percent.
Because the Diamond Creek is quite close to Lake Mead, we used the flow rate for that area in our calculations.

Outflow:

Abstract the overall shape of the lake to be a frustum.

Consider temperature of the lake as well

Height of water changes surface area which changes evaporation rate

The outflow rates of the Hoover Dam is found here: https://www.nps.gov/lake/learn/nature/overview-of-lake-mead.htm#:~:text=Lake%20Mead%20is%20fed%20by,miles%20upstream%20of%20Hoover%20Dam. This gives us the total outflow rate for the past 12 months: 7.3 x 10^6 * 43559.9 ft^3 per year. This can be converted all the way to cfs and m^3 / s, which is 10083.3102 cfs = 285.53 m^3.

The mean depth of the lake is 55.5 m (https://www.nps.gov/lake/learn/nature/overview-of-lake-mead.htm#:~:text=Lake%20Mead%20is%20fed%20by,miles%20upstream%20of%20Hoover%20Dam)

Lake mead is also partially fueled by Las Vegas wash, at 287 cfs (https://www.nps.gov/lake/learn/nature/overview-of-lake-mead.htm#:~:text=Lake%20Mead%20is%20fed%20by,miles%20upstream%20of%20Hoover%20Dam) [note: we didn't include this in the actual code]

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


### Volume calculations

L = 10,000 m

max_base = 64,000 m


### We also don't know x_s and x, since none of us are super famiilar with the concept of humidity.

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

https://www.engineeringtoolbox.com/docs/documents/816/psychrometric_chart_29inHg.pdf is the psychrometric chart in high res. 7000 grains = 1 pound


I ended up using the **psychrometric chart** (per emily's suggestion, thank you emily) to find the relationship between relative humidity, which I can easily google, and air temperature, which I can also easily google. I got 3 points for each month to get a nice spread of datapoints across the year, and for each point, I found the approximate value of the humidity ratio. This will then be converted into a ratio vs. time (days) plot. **In future iterations, it would be good to have more datapoints across multiple years to generate a more accurate model**.

We just need one value for the humidity ratio for the MVP. For this, we will use an average relative humidity and dry bulb temperature for the month of July, since that's the hottest month for Lake Mead. 

According to https://www.weatherwx.com/climate-averages/az/lake+mead.html, the average humidity in July was 21%. The temperature ranged from 83 to 100 degrees Fahrenheit, so to meet in the middle, we have 91.5 degrees. Following the psychrometric chart, we now have 45 GRAINS OF MOISTURE PER POUND OF DRY AIR for our humidity ratio. There are 7000 grains in one pound, so the ratio is 45/7000 = 0.00642857143.


Some things to note for future iterations:
* the moisture holding capacity of air increases dramatically with temperature https://www.engineeringtoolbox.com/moisture-holding-capacity-air-d_281.html. So the humidity ratio equations may be inaccurate at higher temperatures.


## Solar panels

"The cost of solar panels per square meter may vary from $40 to $110" (https://www.solarpowerfam.com/cost-of-solar-panels-per-square-meter/). We decided to take the midpoint of this range, which was $75 per square meter.

The cost of water in Lake mead will need to be decided using personal intuition. 25 million ppl get water from the lake (https://www.nytimes.com/2022/07/22/climate/lake-mead-level-pictures.html#:~:text=Lake%20Mead%2C%20the%20largest%20reservoir,the%20country's%20largest%20agricultural%20valleys). 

"on average, each person uses about 80-100 gallons of water per day" (https://www.usgs.gov/special-topics/water-science-school/science/water-qa-how-much-water-do-i-use-home-each-day). Let's say 90 gallons is typical (to abstract this to a single number). 90 gallons = 0.340687 m^3 of water used per person per day. Therefore, the total amount of water from Lake Mead that is used each day is 25000000*0.340687 = 8517175 m^3.

Now let's find the cost of water bills in the states that get water from lake mead. These states are California, Arizona, Colorado, Utah, New Mexico, Nevada and Wyoming (https://www.kunc.org/environment/2022-07-19/on-the-colorado-river-the-feds-carry-a-big-stick-will-the-states-get-hit#:~:text=That%20infrastructure%20includes%20the%20Colorado,New%20Mexico%2C%20Nevada%20and%20Wyoming). The water bills for these states is 77, 64, 39, 38, 32, 26, 53 (https://worldpopulationreview.com/state-rankings/water-prices-by-state). Taking the average of this gives 47 dollars per month, or 1.51612903 dollars per day. If each person uses 0.340687 m^3 of water per day, then 0.340687 m^3 of water is worth $1.51612903. This means that each cubic meter of water is worth $4.45021099. Each day, the 25 million people spend 8517175 * 4.45021099 = $37903225.8 on water. 

Standard 400W solar panels produce 1800 Watts per hour (https://www.solar.com/learn/how-much-energy-does-a-solar-panel-produce/). 
Although this is impacted by the day-night cycle, we'll abstract this to having constant production. With 86400 seconds per day, the panel

400W solar panels are typically 72-cell (https://news.energysage.com/what-is-the-power-output-of-a-solar-panel/), which is 3.25 feet by 6.42 feet (https://airisenergy.us/solar-panels-dimensions/#:~:text=The%20average%2072%2Dcell%20solar,60%2Dcell%20standard%20size%20panels.) 3.25 feet by 6.42 feet = 20.865 ft^2 = 1.93842193 m^2. 1.93842193 m^2 of solar panels produces 1.8 kWatt-hours per day. Therefore, 1 square meter of panels produces 0.92859 kwh per day. We need units of Watt-hours per second, because the linear space for the ODE is every second. 0.92859 / 3600 = 0.000257941667 kwh/s. Each square meter produces 0.000257941667 kwh per second.

Electricity costs (Cents per kwh) by state are found here: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a. For California, Arizona, Colorado, Utah, New Mexico, Nevada and Wyoming: 24.19, 11.98, 12.51, 9.43, 11.31, 11.58, 8.51. The average of these values is: 89.51/7 = 12.7871428571 cents / kwh. Now we can find the price of how much energy one square meter of panels can generate. 12.7871428571 cents / kwh * 0.000257941667 kwh / s = **0.00329833694 cents per second, for one square meter**.


Again we need units in seconds, so (12.7871428571 cents / kwh) * (1 kwh / 3600 kws) * (1 kws / 1000 w/s) = 0.00000355198413 cents/W-s = 0.0000000355198413 dollars per W/s. This is the average value of electricity. We can figure out how much revenue one squre meter of panels generates from the electricity it produces. 0.0000000355198413 $/(W/s) * 0.257941667 (W/s) / m^2 = 9.16204708 * 10^-9 $/m^2.



# Action items
make a stock and flow diagram
- make a baseline lake model without solar panels (do this together)
Rain -> streams/rivers -> lake mead -> evaporation and dam outflow

create a system of equations to solve lake volume and height as a function fo time


SATURDAY, OCT 15
Cost of solar panels - money we get from selling the energy

^Compare to the lost value of the water evaporating

This tells us if it's worth it to spend the money on panels

Sweep through volume rn for how many solar panels vs ___

Look into conversion factors for how much lost water is worth to us. How much solar generation 

Lily: keep wroking on report

Brooke: get plotly working. Put code into jupyter notebook


# Resources
Put useful websites or libraries in here!

https://plotly.com - a plotting library (?) that bill fan claims is way better than matplot lib

https://www.nps.gov/lake/learn/monitoring-the-river.htm - Colorado river stats. Bottom of page has nice links to charts

https://www.solarpowerfam.com/cost-of-solar-panels-per-square-meter/ - Solar panel pricing by square meter

https://www.usbr.gov/lc/region/g4000/hoover.pdf - hoover dam daily avg releases

https://www.usbr.gov/lc/region/g4000/24mo.pdf - hoover dam monthly avg release flow (and evaporation loss data)

??? - rate of evaporation formula
