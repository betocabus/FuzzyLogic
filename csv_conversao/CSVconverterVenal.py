import pandas as pd

#convert comma to dot and float
def convert_comma_dot(cell):
    converted = float(cell.replace(",","."))
    return converted

df = pd.read_csv("bd/masked_cpf_seq_imob_recolhimento_valor_venal_csv.csv", header=0, sep=",", converters={'valor_venal':convert_comma_dot})

df.to_csv("bd/ServidoresImobVenal.csv", sep=",", index=False, columns=['hash_cpf', 'sequencial_imobiliario', 'valor_venal'])
