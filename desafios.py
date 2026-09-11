qtd_lamp_sala = input("quantas lampadas tem na sala?")
qtd_lamp_sala = int(qtd_lamp_sala)
qtd_lamp_quarto = input("quantas lampadas tem na quarto?")
qtd_lamp_quarto = int(qtd_lamp_quarto)
consumo_por_lampada = 0.57
qtd_horas = input("quantas horas as lampadas ficam acesas por dia?")
qtd_horas = int(qtd_horas)
qtd_dias = 30


consumo_por_dia = (qtd_lamp_sala + qtd_lamp_quarto) * consumo_por_lampada * qtd_horas
total = consumo_por_dia * qtd_dias
total = round(total, 2)


print("em uma casa com", qtd_lamp_sala + qtd_lamp_quarto, "lampadas, que ficam acesas por", qtd_horas, "horas por dia, o consumo mensal é de", total, "R$")