import pandas as pd
import ShapeEXYZ as Sh
import WvalueCalculator as WC
import os




Echoix = input("en eV:")
Nions = int(input("nombre ions envoyé:"))
askModif = input("modif?Y/N")


fichier = "EXYZ" + Echoix + "eV.xlsx"
tableau = pd.read_excel(fichier)

if askModif == "Y":
    modif = True
else:
    modif = False


if modif == True:
    new = Sh.changelabel(tableau)
    new = Sh.separateurIons(new)
    new = Sh.dEtotCol(new)
    new = Sh.dEelectronique(new)
    new = Sh.dxCol(new)
    new = Sh.distanceTrace(new)

    new.to_excel(fichier, index=False, engine='openpyxl')

else:
    new = tableau

Emoy, N = WC.pairsCounter(new,Nions)
print("nombre de pairs moyen par particules =",N,"\nEmoy =",Emoy,"eV")
os.system("pause")