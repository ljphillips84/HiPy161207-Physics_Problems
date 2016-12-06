# Analysing a solar cell with Python - Part 1

When testing solar cell efficiency, we often measure its current-voltage response. During this measurement, a solar cell has a scanned voltage across it while the current response is measured in the light. 1-1.txt is the raw data from such a measurement.

In this exercise we will import some data and extract these parameters:

* Voc
* Jsc
* Fill Factor
* Efficiency

[Additional examples for tasks 1 & 2 can be found here](https://nbviewer.jupyter.org/github/hipyliv/py4sci/blob/master/py4sci.ipynb?force_cache=True)

## Task 1 - Importing the data

Import the data 1-1.txt into an array. numpy's `np.loadtxt()` is a simple method to achieve this (make sure you `import numpy as np`) or use the csv library as in the linked examples.

The raw data is in two columns, the first is voltage in volts, the second is current in amps. Conventionally, we plot the current density (mA/cm^2), not current (A).

Fill in the `i_to_j()` function to convert current to current density : `J = 1000*I/cell area`. The 1000 is to convert to mA and in this instance, the cell area was 0.1 cm^2. The function should loop over every entry in the results and replace the current with current density:
 
 ```python
 for entry in results:
    entry[1] = entry[1] multiplied by the conversion factor
 ```
 This will take the second part of each entry (i.e. the current), convert it to current density, and reassign it to the original place in the array.

## Task 2 - Plotting the data

We will use matplotlib to plot our data, so firstly make sure we are importing this library: `import matplotlib.pyplot as plt`

Use the additional examples given above, or examples from the web, to plot the data. Note you will need to split up the data into x and y. You can do this by looping over the data and appending the first part to an x array and the second to a y array. 
 
 ```python
 for entry in results:
    x_array.append(entry[0])
    y_array.append(entry[1])
```

We can now use `plt.plot(x_array, y_array)` to create the plot.

Play around with the various options from matplotlib to add `plt.xlabel()`, `plt.ylabel()`, `plt.title()` etc...  

Use `plt.show()` to see the result


## Task 3 - Extracting open circuit voltage (Voc)

Complete the `getVoc()` function to return the Voc of the device. This will be the voltage at which the current is closest to zero.

There are many ways to achieve this, for example:

1. Start at one end of the array with a voltage, iterate over the rest of the array and replace the initial value with the new one, only if the corresponding current value is closer to zero.
2. Create a new array of absolute current values and use the index of the minimum value i.e. `array.index(min(array))` to find the voltage at the lowest current.
3. .... whatever else you can think of!

## Task 4 - Extracting short circuit current (Jsc)

Use the `getVoc` function and adapt it to find the Jsc. In a similar way, this is the current at which the voltage is closest to zero.

## Task 5 - Extracting fill factor (FF) and working out the efficiency of the cell

To work out the fill factor, you need to use the following formula: `FF = maximum_power/(Voc * Jsc)` Create an array of powers, using the following (i.e. power = voltage * current): 

```python
for entry in results:
    power.append(abs(entry[0]*entry[1]))
```
Find the maximum entry, and divide it by the Voc and Jsc, which we can obtain using the getVoc and getJsc functions or pass into the fill factor function, alongside the data array e.g.:

```python
def getFF(data, Voc, Jsc):
    #
    # code goes here
    #
    return ff
```

Finally, the efficiency can be found by: `Eff = Voc * Jsc * FF`
