import pandas as pd

def pairsCounter(data,nombreions):
    Npairs = 0
    Energy = []
    Wmoy = 0

    for value in data["dE electronique (en eV)"]:
        if 13<value<200:
            Npairs += 1
            Energy.append(value)
        
        elif value>200:
            Npairs +=2
            Energy.append(value)

    for i in Energy:
        Wmoy += i

    Wmoy = Wmoy/Npairs
    N=Npairs/nombreions

    return Wmoy, N