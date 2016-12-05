import csv
import matplotlib.pyplot as plt
import numpy as np

def getVoc(results):
    modCurrents = []
    for entry in results:
        modCurrents.append(abs(entry[1]))
    return(results[modCurrents.index(min(modCurrents))][0])

def getJsc(results):
    modVoltages = []
    for entry in results:
        modVoltages.append(abs(entry[0]))
    return(results[modVoltages.index(min(modVoltages))][1])

def getFF(results, Voc, Jsc):
    power = []
    for entry in results:
        power.append(entry[0]*entry[1])
    return(min(power)/(Voc*Jsc))

def getEff(Voc, Jsc, FF):
    return(Voc*Jsc*FF)

results = []
with open('1-1.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(str(row[0]).split())

for i in range(0,len(results)):
    results[i][0] = float(results[i][0])

for i in range(0,len(results)):
    results[i][1] = 1000*float(results[i][1])/0.1

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
#plt.savefig("test.png")
plt.show()


print(results)
print("Voc = " + str.format('{0:.2f}', getVoc(results)) + " V")
print("Jsc = " + str.format('{0:.1f}', getJsc(results)) + " mA cm^-2")
print("FF = " + str.format('{0:.1f}', 100*getFF(results, getVoc(results), getJsc(results))) + "%")
print("Eff = " + str.format('{0:.1f}', getEff(getVoc(results), getJsc(results), getFF(results, getVoc(results), getJsc(results)))) + "%")

