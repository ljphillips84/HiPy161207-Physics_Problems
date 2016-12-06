import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def getparameters(data):
    modCurrents = []
    modVoltages = []
    power = []

    for entry in data:
        modCurrents.append(abs(entry[1]))
        modVoltages.append(abs(entry[0]))
        power.append(entry[0] * entry[1])

    Vocsubset = data[max(modCurrents.index(min(modCurrents))-1,0):(modCurrents.index(min(modCurrents))+2)][0:3]
    Voc = abs(stats.linregress(Vocsubset)[1]/stats.linregress(Vocsubset)[0])

    Jscsubset = data[max(modVoltages.index(min(modVoltages)) - 1, 0):(modVoltages.index(min(modVoltages)) + 2)][0:3]
    Jsc = abs(stats.linregress(Jscsubset)[1])

    FF = abs(min(power)/(Voc*Jsc))

    Rs = 1000/abs(stats.linregress(Vocsubset)[0])

    Rsh = 1000/abs(stats.linregress(Jscsubset)[0])

    return Voc*Jsc*FF, Voc, Jsc, FF, Rs, Rsh

def i_to_j(data):
    for i in range(0, len(data)):
        data[i][1] = 1000 * float(data[i][1]) / 0.1
    return data

results = i_to_j(np.loadtxt("1-1.txt"))

voltages = []
currents = []
for entry in results:
    voltages.append(entry[0])
    currents.append(entry[1])

plt.plot(voltages, currents)

plt.xlabel('Voltage (V)')
plt.ylabel('Current Density (mA cm^-2)')
plt.title('J-V Curve')
plt.grid(True)
plt.axhline(0, linewidth="2", color="black")
plt.axvline(0, linewidth="2", color="black")
plt.savefig('1-1.png')
plt.show()

print("Eff = " + str.format('{0:.2f}', getparameters(results)[0]) + "%")
print("Voc = " + str.format('{0:.3f}', getparameters(results)[1]) + " V")
print("Jsc = " + str.format('{0:.2f}', getparameters(results)[2]) + " mA cm^-2")
print("FF = " + str.format('{0:.2f}', 100*getparameters(results)[3]) + "%")
print("Rs = " + str.format('{0:.2f}', getparameters(results)[4]) + " Ohm cm^-2")
print("Rsh = " + str.format('{0:.2f}', getparameters(results)[5]) + " Ohm cm^-2")
