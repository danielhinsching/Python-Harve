renda = float(input("qual sua renda mensal? "))

if renda <= 1903.98:
      print("isento")
else:
      if renda <= 2826.65:
            print("aliquota de 7,5%")
      else:
            if renda <= 3751.05:
                  print("aliquota de 15%")
            else:
                  if renda <= 4664.68:
                        print("aliquota de 22,5%")
                  else:
                        print("aliquota de 27,5%")