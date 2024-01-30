import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd



def SumRiemann(talbeau,xcol,ycol):
    int_value = 0

    for i in range(0,len(tableau)-1):
        width = tableau.iat[i,xcol] - tableau.iat[i+1,xcol]
        height = ((tableau.iat[i,ycol] + tableau.iat[i+1,ycol])/2)

        A = abs(width*height)
        int_value += A
    
    return int_value



fichier = "tab25.xlsx"
tableau = pd.read_excel(fichier)
xcolions = 0
ycolions = 1

xcolrecoils = 0
ycolrecoils = 2

Riemanions = SumRiemann(tableau,xcolions,ycolions)*10**-3
RiemanRecoils = SumRiemann(tableau,xcolrecoils,ycolrecoils)*10**-3

trapzions = np.trapz(tableau["IONS"], x=tableau["(Ang)"])*10**-3
trapzrecoils = np.trapz(tableau["RECOILS"], x=tableau["(Ang)"])*10**-3

texte = "E tot loss ionisation ions : \n Somme Riemman =",Riemanions,"KeV \n trapz int = ",trapzions,"KeV \n E tot loss ionisation recoils : \n Somme Riemman =",RiemanRecoils,"KeV \n trapz int = ",trapzrecoils,"KeV","\n E loss ionisation total = ",trapzions + trapzrecoils

fichier = open("result.txt", "a")
fichier.write(texte)
fichier.close()


#print("E tot loss ionisation recoils : \n Somme Riemman =",RiemanRecoils,"KeV \n trapz int = ",trapzrecoils,"KeV")
#print("E loss ionisation total = ",trapzions + trapzrecoils)