import pandas as pd

df = pd.read_csv("bd/ServidoresImobVenal.csv", header=0, sep=",")

g = df.groupby('sequencial_imobiliario')
max = g.max()

max.to_csv("ServidoresImobVenal.csv", sep=",", index=False, columns=['hash_cpf', 'sequencial_imobiliario', 'valor_venal'])
