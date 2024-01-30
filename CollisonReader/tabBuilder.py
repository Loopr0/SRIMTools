import pandas as pd

def createTab(fichier,Nom):
    None
    df = pd.read_csv(fichier, sep = " ")
    da = pd.DataFrame(df)
    da.to_csv(Nom + ".csv")