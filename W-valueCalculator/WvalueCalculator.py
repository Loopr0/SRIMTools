import pandas as pd


def createdE(data):
    data["dE loss ionisation"]


def pairsCounter(data,nombreions):
    Npairs = 0
    Energy = []
    Wmoy = 0

    for value in data["dE loss ionisation"]:
        if 10<value<150:
            Npairs += 1
            Energy.append(value)
        
        elif value>150:
            Npairs +=2
            Energy.append(value)

    for i in Energy:
        Wmoy += i

    Wmoy = Wmoy/Npairs
    N=Npairs/nombreions

    return Wmoy, N




Echoix = input("en eV:")
Nions = int(input("nombre ions envoyé:"))

fichier = "EXYZ400eVmodif.xlsx"
#"tab" + Echoix + "eV.xlsx"
data = pd.read_excel(fichier)


W, N = pairsCounter(data,Nions)  
print("nombre de pairs tot pour 100 particules =",N,"\nW-value =",W,"eV")
    
