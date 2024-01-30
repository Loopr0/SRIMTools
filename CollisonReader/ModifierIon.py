import shutil as sh


def supprimer_ligneI(fichier,ligne_suppr):
    with open(fichier, 'r') as file:
        lignes = file.readlines()

        del lignes[ligne_suppr -1]

        with open(fichier, 'w') as file:
            file.writelines(lignes)



def choixLigneI(fichier):
    numLigne = 0
    Ligne_suppr = []
    Summ_suppr = []

    with open(fichier, 'r') as file:
        for ligne in file:

            numLigne += 1
            Ligne_suppr.append(numLigne)

            splitligne = ligne.split()


            for mot in splitligne:
                if mot == "Summary":
                    Summ_suppr.append(numLigne)
                
                if mot == "³":
                    Ligne_suppr.remove(numLigne)
            
            

    Ligne_suppr += Summ_suppr
    
                    

    return Ligne_suppr


def modif_caracI(fichier):
    with open(fichier, 'r') as file:
        contenu = file.read()

        contenu_modifie = contenu.replace("³ <== Start of New Cascade  ³","").replace(",",".").replace("³  "," ").replace("³ "," ").replace(" ³"," ").replace("³"," ")
        contenu_modifie = "IonNumb Energy(KeV) Depth(A) LateralY DistanceZ(A) Se(eV/A) AtomHit RecoilEnergy(eV)\n" + contenu_modifie

    with open(fichier, 'w') as filemodif:
        filemodif.write(contenu_modifie)
