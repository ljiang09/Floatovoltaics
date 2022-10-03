# QEA 3 Mini Project 1 Proposal

**1. Which project are you doing?**

Project 2 (Floatovoltaics)

**2. What are you investigating in particular?**

How does the cost-effectiveness of floatovoltaics vs shade balls compare?

**3. [Skip this question if doing Option 4a.] How are you going to model the system? Start answering this question by telling us the following:**

The system consists of water flowing from the Colorado River into Lake Mead and water flowing from Lake Mead out of Lake Mead. We will be modeling the input water, the output water, and the water stored in Lake Mead.

The main ODE will represent the volume of water in Lake Mead. It is of the form dV/dt+P(t)V=Q(t), where t is time and V is volume of water.

We will be using a system of first-order linear ODE’s, which will be coupled. The input flow of water would impact the amount of water stored in the lake, which would in turn impact the amount of water being evaporated (which again impacts the amount of water stored in the lake).

**4. What do you hope to learn from this project? You might consider both quantitative and non-quantitative skills.**

Quantitative:
* Increase comfort with creating and solving for ODEs
* Learn how to use Python modeling libraries such as Plotly

Qualitative:
* Learn about floatovoltaics
* Learn about shade balls

**5. When will your group do this work? We'd like to see both milestones/deadlines and specific times you are planning to work together. Note: We will dedicate some (but not all) time during each class to unstructured project work.**

Milestones:
MVP - Complete by end of class on the 6th:
* Simplified version of the ODE where inputs are constants
* Create more complex geometry for the lake itself (frustum)
* Contains the math for the basic model & the solar panels

Iteration 1 - Complete on 13th
* Model the inputs as the flow rate of the Colorado River
* Model the output as the dam ODE
* Add calculations for shade balls/other potential options
All work above will be done in class

Iteration 2 - Complete over the weekend (10/14-10/16; most likely on 10/16)
* Have the model change during the seasons to account for varying water levels

Final deliverable: 17th

**6. Do you have any concerns about this project? If so, what will you do to mitigate those concerns? Is there anything you need from the teaching team?**

Sleep schedule (Lily & Aditi); to mitigate this, we will set our work times to start at reasonable hours & we will also encourage Lily & Aditi to set more alarms.
