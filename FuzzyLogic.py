import pandas as pd
import numpy as np
import skfuzzy as fuzz

#códigos de fuzzy começam aqui
def Incompatibilidade(salarioVal, tempoSVal, patrimonioVal):
    #entradas
    salario = np.arange(0, 1000001, 1)
    tempoS = np.arange(0, 101, 1)
    patrimonio = np.arange(0, 10000001, 1)
    incomp = np.arange(0, 101, 1)

    #pertinência
    salario_Mbaixo = fuzz.trapmf(salario, [0, 0, 800, 1000])
    salario_baixo = fuzz.gaussmf(salario, 2200,1000)
    salario_medio = fuzz.gaussmf(salario, 4000,1500)
    salario_alto = fuzz.trapmf(salario, [5500, 7000, 100000, 100000])

    tempo_pouco = fuzz.trapmf(tempoS, [0, 0, 3, 5])
    tempo_moderado = fuzz.trapmf(tempoS, [3, 7, 15, 20])
    tempo_muito = fuzz.trapmf(tempoS, [15, 30, 100, 100])

    patrimonio_pequeno = fuzz.trapmf(patrimonio, [0, 0, 35000, 60000])
    patrimonio_medio = fuzz.gaussmf(patrimonio, 330000,300000)
    patrimonio_grande = fuzz.trapmf(patrimonio, [400000, 10000000, 10000000, 10000000])

    incomp_baixa = fuzz.trapmf(incomp, [0, 0, 15, 35])
    incomp_media = fuzz.trapmf(incomp, [30, 40, 60, 70])
    incomp_alta = fuzz.trapmf(incomp, [60, 80, 100, 100])

    #salarioVal = 900
    #tempoSVal = 4
    #patrimonioVal=100000

    #interpola as variáveis
    salario0 = fuzz.interp_membership(salario, salario_Mbaixo, salarioVal)
    salario1 = fuzz.interp_membership(salario, salario_baixo, salarioVal)
    salario2 = fuzz.interp_membership(salario, salario_medio, salarioVal)
    salario3 = fuzz.interp_membership(salario, salario_alto, salarioVal)
    tempo0 = fuzz.interp_membership(tempoS, tempo_pouco, tempoSVal)
    tempo1 = fuzz.interp_membership(tempoS, tempo_moderado, tempoSVal)
    tempo2 = fuzz.interp_membership(tempoS, tempo_muito, tempoSVal)
    patrimonio0 = fuzz.interp_membership(patrimonio, patrimonio_pequeno, patrimonioVal)
    patrimonio1 = fuzz.interp_membership(patrimonio, patrimonio_medio, patrimonioVal)
    patrimonio2 = fuzz.interp_membership(patrimonio, patrimonio_grande, patrimonioVal)

    # Determinando as regras:

    # RULE0: SALARIO MUITO BAIXO E PEQUENO PATRIMONIO OU MEDIO PATRIMONIO OU GRANDE PATRIMONIO … INCOMPATÕVEL
    # salario0 && (tempo0 || tempo1) && (patrimonio0 || patrimonio1 || patrimonio2)

    rule0_0 = np.fmax(patrimonio0, patrimonio1)  # patrimonio0 || patrimonio1
    rule0_1 = np.fmax(rule0_0, patrimonio2)  # patrimonio0 || patrimonio1 || patrimonio2
    rule0 = np.fmin(rule0_1, salario0)  # patrimonio0 || patrimonio1 || patrimonio2 && salario0

    # RULE1: SALARIO BAIXO E POUCO TEMPO DE SERVICO E PATRIMONIO PEQUENO OU MODERADO OU GRANDE … INCOMPATÕVEL

    rule1_0 = np.fmax(patrimonio1, patrimonio2)  # patrimonio0 || patrimonio1
    rule1_1 = np.fmax(rule1_0, patrimonio0)  # patrimonio0 || patrimonio1 || patrimonio2
    rule1_2 = np.fmin(rule1_1, tempo0)  # patrimonio0 || patrimonio1 || patrimonio2 && tempo0
    rule1 = np.fmin(rule1_2, salario1)  # patrimonio0 || patrimonio1 || patrimonio2 && tempo0 && salario1

    # RULE2: SALARIO BAIXO E TEMPO MODERADO E MEDIO PATRIMONIO OU GRANDE PATRIMONIO … INCOMPATIVEL

    rule2_0 = np.fmax(patrimonio1, patrimonio2)  # patrimonio0 || patrimonio1
    rule2_1 = np.fmin(rule2_0, tempo1)  # patrimonio0 || patrimonio1 && tempo1
    rule2 = np.fmin(rule2_1, salario1)  # patrimonio0 || patrimonio1 && tempo1 && salario1

    # RULE3: SALARIO BAIXO E MUITO TEMPO DE SERVI«O E GRANDE PATRIMONIO … INCOMPATIVEL

    rule3_0 = np.fmin(patrimonio2, tempo2)  # patrimonio2 && tempo2
    rule3 = np.fmin(rule3_0, salario1)  # patrimonio2 && tempo2 && salario1

    # RULE4: SALARIO MEDIO E POUCO TEMPO DE SERVICO E MODERADO PATRIMONIO OU GRANDE PATRIMONIO … INCOMPATIVEL

    rule4_0 = np.fmax(patrimonio1, patrimonio2)  # patrimonio1 || patrimonio2
    rule4_1 = np.fmin(rule4_0, tempo1)  # patrimonio1 || patrimonio2 && tempo1
    rule4 = np.fmin(rule4_1, salario2)  # patrimonio1 || patrimonio2 && tempo1 && salario2

    # RULE5: SALARIO MEDIO E MODERADO TEMPO OU POUCO TEMPO E GRANDE PATRIM‘NIO … INCOMPATIVEL

    rule5_0 = np.fmax(tempo0, tempo1)  # tempo0 || tempo1
    rule5_1 = np.fmin(rule5_0, patrimonio2)  # tempo0 || tempo1 && patrimonio2
    rule5 = np.fmin(rule5_1, salario2)  # tempo0 || tempo1 && patrimonio2 && salario2

    # RULE6: SALARIO ALTO E POUCO TEMPO OU MEDIO TEMPO E GRANDE PATRIMONIO … INCOMPATIVEL

    rule6_0 = np.fmax(tempo0, tempo1)  # tempo0 || tempo1
    rule6_1 = np.fmin(rule6_0, patrimonio2)  # tempo0 || tempo1 && patrimonio2
    rule6 = np.fmin(rule6_1, salario3)  # tempo0 || tempo1 && patrimonio2 && salario3

    # FINAL RULE: INCOMPATIBILIDADE
    final_rule = np.fmax(rule0, np.fmax(rule1, np.fmax(rule2, np.fmax(rule3, np.fmax(rule4, np.fmax(rule5, rule6))))))

    incomp0 = rule0 * incomp_media
    incomp1 = rule1 * incomp_media
    incomp2 = rule2 * incomp_media
    incomp3 = rule3 * incomp_media
    incomp4 = rule4 * incomp_media
    incomp5 = rule5 * incomp_media
    incomp6 = rule6 * incomp_media

    #final_rule2 = np.fmax(incomp0, np.fmax(incomp1, np.fmax(incomp2, np.fmax(incomp3, np.fmax(incomp4, np.fmax(incomp5, incomp6))))))
    #incompat = fuzz.defuzz(incomp, final_rule2, 'centroid')

    return round((final_rule*100),3)
#fim fuzzy logic

#Salvar Incompatibilidade no CSV
df = pd.read_csv("group5.csv", header=0, sep=",")

linhas = df.shape[0]
for x in range(0, linhas):
    g = Incompatibilidade(df.valor_bruto_mensal_para_o_mes_de_ref[x], df.data_cargo[x], df.valor_venal[x])

    print("Servidor: " + str(df.hash_cpf[x]) + "       Incompatibilidade: " + str(g) + " %")

    df.at[x, 'incompatibilidade_servidor'] = g

df.to_csv("Incompatibilidade_servidores.csv", sep=",", index=False, columns=['hash_cpf', 'valor_venal','carga_horaria_semanal','data_cargo','valor_bruto_mensal_para_o_mes_de_ref','incompatibilidade_servidor'])
