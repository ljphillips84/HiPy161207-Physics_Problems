import numpy as np
import os
import matplotlib.pyplot as plt
import jvanalysis as jv

for directory, subdirectories, files in os.walk('/home/ljp84/git-repos/HiPy161207-Physics/'):
    for file in files:
        if file[-4:] == ".txt" and file[1] == "-":

            results = jv.i_to_j(np.loadtxt("1-1.txt"))

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
            #plt.savefig(str(file[0:3])+'.png')
            #plt.show()

            print("Eff = " + str.format('{0:.2f}', jv.getparameters(results)[0]) + "%")
            print("Voc = " + str.format('{0:.3f}', jv.getparameters(results)[1]) + " V")
            print("Jsc = " + str.format('{0:.2f}', jv.getparameters(results)[2]) + " mA cm^-2")
            print("FF = " + str.format('{0:.2f}', 100 * jv.getparameters(results)[3]) + "%")
            print("Rs = " + str.format('{0:.2f}', jv.getparameters(results)[4]) + " Ohm cm^2")
            print("Rsh = " + str.format('{0:.2f}', jv.getparameters(results)[5]) + " Ohm cm^2")
