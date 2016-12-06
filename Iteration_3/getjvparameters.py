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

    Jscsubset = data[max(modVoltages.index(min(modVoltages)) - 5, 0):(modVoltages.index(min(modVoltages)) + 6)][0:3]
    Jsc = abs(stats.linregress(Jscsubset)[1])

    FF = abs(min(power)/(Voc*Jsc))

    Rs = 1000/abs(stats.linregress(Vocsubset)[0])

    Rsh = 1000/abs(stats.linregress(Jscsubset)[0])

    return Voc*Jsc*FF, Voc, Jsc, FF, Rs, Rsh