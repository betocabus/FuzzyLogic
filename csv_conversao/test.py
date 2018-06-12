import pandas as pd

df = pd.read_csv("group4.csv", header=0, sep=",")

g = df.valor_venal.max()

print(g)
#g.to_csv("group4.csv", index=False, sep=",", columns=['hash_cpf', 'valor_venal' , 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])
