import pandas as pd

df = pd.read_csv("ServidoresImobVenal.csv", header=0, sep=",")

g = df.groupby('hash_cpf')
max = g.sum()

max.to_csv("ServidoresImobVenal2.csv", sep=",", columns=['hash_cpf', 'valor_venal'])
