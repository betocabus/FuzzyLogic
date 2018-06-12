import pandas as pd

df = pd.read_csv("group3.csv", header=0, sep=",")

g = df[df.valor_venal != 0]

print(g.hash_cpf)
g.to_csv("group4.csv", index=False, sep=",", columns=['hash_cpf', 'valor_venal' , 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])
