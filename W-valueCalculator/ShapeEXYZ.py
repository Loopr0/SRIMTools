import pandas as pd
import numpy as np

def changelabel(df):
    df.columns.values[0] = "Ion Number"
    df.columns.values[1] = "Energy (keV)"
    df.columns.values[2] = "X (Angstrom)"
    df.columns.values[3] = "Y (Angstrom)"
    df.columns.values[4] = "Z (Angstrom)"
    df.columns.values[5] = "Electronic Stop.(eV/A)"
    df.columns.values[6] = "Energy lost to Last Recoil(eV)"

    return df

def distanceTrace(df):
    df.at[0,"distance parcourue trace (angstrom)"] = 0
    for index in range(1,len(df)):
        df.at[index,"distance parcourue trace (angstrom)"] = df.at[index-1,"distance parcourue trace (angstrom)"] + df.at[index,"dx (angstrom)"]
    return df


def separateurIons(df):
    memory = 1
    emptyrow = pd.Series({})

    for index in range(0,len(df)+df.loc[len(df)-1, "Ion Number"]-1):
        a= df.loc[index, "Ion Number"]

        if a != memory:
            df = pd.concat([df.iloc[:index], emptyrow.to_frame().T, df.iloc[index:]]).reset_index(drop=True)
        memory = a

    df = df.reset_index(drop=True)

    return df

def dEtotCol(df):
    for index in range(1,len(df)):

        df.at[index,"dE tot (en eV)"] = (df.at[index-1,"Energy (keV)"] - df.at[index,"Energy (keV)"])*10**3

    return df


def dxCol(df):
    for index in range(1,len(df)):
        df.at[index,"dx (angstrom)"] = np.sqrt((float(df.at[index,"X (Angstrom)"]) - float(df.at[index-1,"X (Angstrom)"]))**2+(float(df.at[index,"Y (Angstrom)"]) - float(df.at[index-1,"Y (Angstrom)"]))**2 + (float(df.at[index,"Z (Angstrom)"]) - float(df.at[index-1,"Z (Angstrom)"]))**2)

    return df

def dEelectronique(df):
    for index in range(1,len(df)):

        df.at[index,"dE electronique (en eV)"] = df.at[index,"dE tot (en eV)"] - df.at[index,"Energy lost to Last Recoil(eV)"]

    return df

