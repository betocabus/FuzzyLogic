import pandas as pd
from datetime import datetime, timedelta

#Convert string in datetime and calculate time of work
def convert_data_cargo(cell):
    dataInicio = datetime.strptime(cell, '%d-%m-%Y').year
    dataFim = datetime.today().year
    data = dataFim-dataInicio
    return data

#convert comma to dot and float
def convert_comma_dot(cell):
    converted = float(cell.replace(",","."))
    return converted

df = pd.read_csv("group4.csv", header=0, sep=";", converters={'data_cargo':convert_data_cargo, 'valor_bruto_mensal_para_o_mes_de_ref':convert_comma_dot})

#df.to_csv("servidores.csv", sep=",", index=False, columns=['hash_cpf', 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])


#servidor = df[df.valor_bruto_mensal_para_o_mes_de_ref>=20000]

servidor = df

#servidor = str(df['valor_bruto_mensal_para_o_mes_de_ref']).replace(",", ".")

rows, columns = df.shape

#servidor.to_csv("servidor.csv", sep=",", index=False, columns=['hash_cpf', 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])

print (servidor)