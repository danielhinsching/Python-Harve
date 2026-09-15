valor = int(input("qual o tamanho?"))
unidade = input("qual a unidade de medida (cm - m))")
valor_final = 0

if unidade == "cm":
      valor_final = valor / 100 
      print("o tamanho em metros é de",valor_final )
else:
      if unidade == "m":
            valor_final = valor * 100
            print("o tamanho em centimetros é de",valor_final )
      else:
            print("a unidade de medida é invalida")