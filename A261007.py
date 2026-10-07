""" Etapa 01: Ler o arquivo com os dados da eleição"""

import pandas as pd

CAMINHO_CSV = "Eleicoes.csv"

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dy)