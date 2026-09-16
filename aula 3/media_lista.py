valores = [11, 22, 51, 86, 12, 71, 63]
soma = 0

for x in valores:
      soma = soma + x
      
      media = soma / len(valores)
      print(f" nossa média é de {round(media, 1)}")