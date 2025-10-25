#Gerenciador de pacotes do python --> PIP

import pandas as pd
import numpy as np

#Criando serie indexada por valor inteiro
serie = pd.Series([10, 20, 43, 87, 3], index=['a', 'b', 'c','d', 'e'])
print(serie)

#transformaando dicionario em uma serie
dicionario = {'Joao': 90, 'maria': 86, 'Andre': 75, 'carla': 94}
serie = pd.Series(dicionario)
print(serie)

#trabalho com valores nulos
dicionario = {'Joao': 90, 'maria': 86, 'Andre': 75, 'carla': 94, 'alex': np.nan}
serie = pd.Series(dicionario)
print(serie)
print(serie.isnull()) #apresenta true ou false

#DataFrame: estrutura bidimencional, utilizada para armazenar dados

aluno = {'nome': ['Joao', 'Maria', 'Carlos', 'Silvia', 'Andre', 'Juliana'],
         'RA': [1000, 2000, 3000, 4000, 2700, 6000],
         'sexo': ['M', 'F', 'M', 'F', 'M', 'F'],
         'nota': [80.0, 90.0, 75.0, 100.0, 96.5, 98.5]
         }
df = pd.DataFrame(aluno)
print(df)
print('\nos 5 primeiros\n', df.head())
print('\nos 5 ultimos\n', df.tail())
print('\nresumo estatistico de todos os campos numericos\n', df.describe())

