import pandas as pd
import numpy as np
import skfuzzy as fuzz
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

#códigos de fuzzy começam aqui

#entradas
salario = np.arange(0, 100, 1)
tempoS = np.arange(0, 100, 1)
patrimonio = np.arange(0, 100, 1)
incomp = np.arange(0, 100, 1)

#pertinência
salario_Mbaixo = fuzz.trapmf(salario, [0, 0, 5, 10])
salario_baixo = fuzz.trapmf(salario, [5, 10, 20, 35])
salario_medio = fuzz.trapmf(salario, [30, 40, 60, 70])
salario_alto = fuzz.trapmf(salario, [60, 80, 100, 100])

tempo_pouco = fuzz.trapmf(tempoS, [0, 0, 15, 35])
tempo_moderado = fuzz.trapmf(tempoS, [30, 40, 60, 70])
tempo_muito = fuzz.trapmf(tempoS, [60, 80, 100, 100])

patrimonio_pequeno = fuzz.trapmf(patrimonio, [0, 0, 15, 35])
patrimonio_medio = fuzz.trapmf(patrimonio, [30, 40, 60, 70])
patrimonio_grande = fuzz.trapmf(patrimonio, [60, 80, 100, 100])

incomp_baixa = fuzz.trapmf(incomp, [0, 0, 15, 35])
incomp_media = fuzz.trapmf(incomp, [30, 40, 60, 70])
incomp_alta = fuzz.trapmf(incomp, [60, 80, 100, 100])



def aggMemberFunc (salarioVal, tempoSVal, patrimonioVal, salario, tempoS, patrimonio, salario_Mbaixo, salario_baixo, salario_medio, salario_alto, tempo_pouco, tempo_moderado, tempo_muito, patrimonio_pequeno, patrimonio_medio, patrimonio_grande, incomp, incomp_baixa, incomp_media, incomp_alta)
#interpola as variáveis
salario0 = fuzz.interp_membership(salario, salario_Mbaixo)
salario1 = fuzz.interp_membership(salario, salario_baixo)
salario2 = fuzz.interp_membership(salario, salario_medio)
salario3 = fuzz.interp_membership(salario, salario_alto)
tempo0 = fuzz.interp_membership(tempoS, tempo_pouco)
tempo1 = fuzz.interp_membership(tempoS, tempo_moderado)
tempo2 = fuzz.interp_membership(tempoS, tempo_muito)
patrimonio0 = fuzz.interp_membership(patrimonio, patrimonio_pequeno)
patrimonio1 = fuzz.interp_membership(patrimonio, patrimonio_medio)
patrimonio2 = fuzz.interp_membership(patrimonio, patrimonio_grande)
# Determina os pesos para cada antecedente
rule0 = np.fmax(salario0, tempo0) #Salario muito baixo e pouco tempo servico
rule1 = np.fmax(salario0, tempo0) #Salario muito baixo e pouco tempo servico


#fim fuzzy logic


df = pd.read_csv("group4.csv", header=0, sep=";", converters={'data_cargo':convert_data_cargo, 'valor_bruto_mensal_para_o_mes_de_ref':convert_comma_dot})

#df.to_csv("servidores.csv", sep=",", index=False, columns=['hash_cpf', 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])


#servidor = df[df.valor_bruto_mensal_para_o_mes_de_ref>=20000]

servidor = df

#servidor = str(df['valor_bruto_mensal_para_o_mes_de_ref']).replace(",", ".")

rows, columns = df.shape

#servidor.to_csv("servidor.csv", sep=",", index=False, columns=['hash_cpf', 'carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref'])

print (servidor)