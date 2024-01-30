import shutil as sh


def supprimer_ligneR(fichier,ligne_suppr):
    with open(fichier, 'r') as file:
        lignes = file.readlines()

        del lignes[ligne_suppr -1]

        with open(fichier, 'w') as file:
            file.writelines(lignes)



def choixLigneR(fichier):
    numLigne = 0
    Ligne_suppr = []

    with open(fichier, 'r') as file:
        for ligne in file:

            numLigne += 1
            Ligne_suppr.append(numLigne)

            splitligne = ligne.split()  

            for mot in splitligne:
                if mot == "Û":
                    Ligne_suppr.remove(numLigne)
                    break
                    


    return Ligne_suppr


def supprimer_caracR(fichier):
    with open(fichier, 'r') as file:
        contenu = file.read()

        contenu_modifie = contenu.replace('Û ','').replace("Û<ÄPrime","").replace("RecoilÛ","").replace("Û","").replace(",",".").replace("   "," ").replace("  "," ")
        contenu_modifie = "Recoil Atom Energy(eV) x(A) y(A) z(A) Vac Repl\n" + contenu_modifie

    with open(fichier, 'w') as filemodif:
        filemodif.write(contenu_modifie)


