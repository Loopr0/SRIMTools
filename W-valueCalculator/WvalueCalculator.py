import pandas as pd

def pairsCounter(data,nombreions):
    Npairs = 0
    Energy = []
    Emoy = 0

    for value in data["dE electronique (en eV)"]:
        if 13<value<150:
            Npairs += 1
            Energy.append(value)
        
        elif 150<value<287:
            Npairs +=2
            Energy.append(value)
        
        elif 287<value<424:
            Npairs +=3
            Energy.append(value)

        elif 424<value<561:
            Npairs +=3
            Energy.append(value)

    for i in Energy:
        Emoy += i

    Emoy = Emoy/Npairs
    N=Npairs/nombreions

    return Emoy, N