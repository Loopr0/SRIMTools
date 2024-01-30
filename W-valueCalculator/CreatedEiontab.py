import pandas as pd


def separateurIons(df):
    memory = 1
    emptyrow = pd.Series({})


    for index in range(0,len(df)):
        a= df.loc[index, 'Ion Number']

        if a != memory:
            print(a,memory)
            df = pd.concat([df.iloc[:index], emptyrow.to_frame().T, df.iloc[index:]]).reset_index(drop=True)
        memory = a

    df = df.reset_index(drop=True)

    return df


Echoix = input("en eV:")
fichier = "EXYZ" + Echoix + "eV.xlsx"
tableau = pd.read_excel(fichier)

new = separateurIons(tableau)

chemin_fichier_excel = 'donnees_modifiees.xlsx'
new.to_excel(chemin_fichier_excel, index=False, engine='openpyxl')

