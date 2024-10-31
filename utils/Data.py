import pandas as pd
import random


All_Data = pd.read_excel("penguins.xlsx")

Species = All_Data["species"].unique()

Species_Data_Frame = All_Data.loc[:, ['species']].values

Features = list(All_Data.columns[1:])

Adelie_Data = All_Data.loc[All_Data["species"] == "Adelie"]

Gentoo_Data = All_Data.loc[All_Data["species"] == "Gentoo"]

Chinstrap_Data = All_Data.loc[All_Data["species"] == "Chinstrap"]


def Extract_Species_Values(data: pd.DataFrame, className: str):
    return data.loc[data["species"] == className].loc[:, [
        'principal component 1', 'principal component 2']].values


def Seperate_Test_Train(data):
    random.shuffle(data)
    x = (len(data)*3)//10
    return data[:x], data[x:]
