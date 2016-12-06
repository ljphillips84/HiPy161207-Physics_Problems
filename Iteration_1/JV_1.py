import matplotlib.pyplot as plt
import numpy as np

def getVoc(data):
    modCurrents = []
    for entry in data:
        modCurrents.append(abs(entry[1]))
    return abs(data[modCurrents.index(min(modCurrents))][0])

def getJsc(data):
    modVoltages = []
    for entry in data:
        modVoltages.append(abs(entry[0]))
    return abs(data[modVoltages.index(min(modVoltages))][1])

def getFF(data):
    power = []
    for entry in data:
        power.append(entry[0]*entry[1])
    return abs(min(power)/(getVoc(data)*getJsc(data)))

def getEff(data):
    return abs(getVoc(data)*getJsc(data)*getFF(data))

def i_to_j(data):
    for i in range(0, len(data)):
        data[i][1] = 1000 * float(data[i][1]) / 0.1
    return data

results = np.loadtxt("1-1.txt")

results = i_to_j(results)

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

print("Voc = " + str.format('{0:.2f}', getVoc(results)) + " V")
print("Jsc = " + str.format('{0:.1f}', getJsc(results)) + " mA cm^-2")
print("FF = " + str.format('{0:.1f}', 100*getFF(results)) + "%")
print("Eff = " + str.format('{0:.1f}', getEff(results)) + "%")
