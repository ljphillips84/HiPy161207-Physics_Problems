import csv
import os

import matplotlib.pyplot as plt

from Iteration_3 import getjvparameters as params

for directory, subdirectories, files in os.walk('/home/ljp84/git-repos/HiPy161207-Physics/'):
    for file in files:
        if file[-4:] == ".txt" and file[1] == "-":
            results = []
            with open(file, newline='') as inputfile:
                for row in csv.reader(inputfile):
                    results.append(str(row[0]).split())

            for i in range(0, len(results)):
                results[i][0] = float(results[i][0])

            for i in range(0, len(results)):
                results[i][1] = 1000 * float(results[i][1]) / 0.1

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
            plt.savefig(str(file[0:3])+'.png')
            #plt.show()

            print("Eff = " + str.format('{0:.2f}', params.getparameters(results)[0]) + "%")
            print("Voc = " + str.format('{0:.3f}', params.getparameters(results)[1]) + " V")
            print("Jsc = " + str.format('{0:.2f}', params.getparameters(results)[2]) + " mA cm^-2")
            print("FF = " + str.format('{0:.2f}', 100 * params.getparameters(results)[3]) + "%")
            print("Rs = " + str.format('{0:.2f}', params.getparameters(results)[4]) + " Ohm cm^2")
            print("Rsh = " + str.format('{0:.2f}', params.getparameters(results)[5]) + " Ohm cm^2")