import pandas as pd

df = pd.read_csv("group.csv", header=0, sep=",")


g = df.groupby('hash_cpf')
max = g.sum()

max.to_csv("group2.csv", sep=",", columns=['hash_cpf', 'valor_venal' , 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])
