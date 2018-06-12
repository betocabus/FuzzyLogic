import pandas as pd

df1 = pd.read_csv("ServidoresImobVenal2.csv", header=0, sep=",")
df2 = pd.read_csv("Servidores.csv", header=0, sep=",")

g = pd.concat([df1,df2])

g.to_csv("group.csv", index=False, sep=",", columns=['hash_cpf', 'valor_venal' , 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])
