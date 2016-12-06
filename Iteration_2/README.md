# Analysing a solar cell with Python - Part 2

In this exercise we will extend our analysis extract additional parameters using the `from scipy import stats` library and the `stats.linregress(sub_array)` function:

* Series resistance
* Shunt resistance

## Series resistance

The series resistance, Rs is taken from the gradient of the J-V curve about the Voc point. The formula can be written as `1000/gradient_at_Voc` where the factor of 1000 is included to take account of our data being in mA.

Find the point in the data for the Voc, generate a small sub-array of points, just several either side of the Voc, and use the `linregress()` function to find the gradient.

## Shunt resistance

The shunt resistance, Rsh is taken from the gradient of the J-V curve about the Jsc point. The formula can be written as `1000/gradient_at_Jsc`.

Find the point in the data for the Jsc, generate a small sub-array of points, just several either side of the Voc, and use the `linregress()` function to find the gradient.

Note, you will require on the first piece of data that the function returns i.e. `linregress()[0]`

## Further idea

Can you also make use of the `linregress()` function to extract a mre accurate Voc and Jsc? Find the actual intercepts with the axes rather than just use the point nearest zero?  
