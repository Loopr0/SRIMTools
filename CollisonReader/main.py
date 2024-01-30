import shutil as sh
import ModifierIon as MI
import ModifierRecoils as MR
import tabBuilder as tb


src = "COLLISON.txt"
FichierRecoils = "recoilsF.txt"
FichierIons = "IonsF.txt"

sh.copy2(src,FichierRecoils)
sh.copy2(src,FichierIons)



########################Recoils##############################

choix = MR.choixLigneR(FichierRecoils)
choix.sort(reverse = True)


for i in choix:
    MR.supprimer_ligneR(FichierRecoils,i)



MR.supprimer_caracR(FichierRecoils)
tb.createTab(FichierRecoils,"TabRecoils")




###########################ION########################


choix = MI.choixLigneI(FichierIons)
choix.sort(reverse = True)


for i in choix:
    MI.supprimer_ligneI(FichierIons,i)



MI.modif_caracI(FichierIons)

tb.createTab(FichierIons,"TabIons")