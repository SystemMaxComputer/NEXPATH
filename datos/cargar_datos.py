import pandas as pd


def save_data(ruta):
    return pd.read_csv(ruta, sep=";",encoding='utf-8')