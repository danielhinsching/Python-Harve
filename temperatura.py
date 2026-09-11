operacao = input("Informe (C ou K) para transformar de celcius para kelvim ou vice versa: ")

if operacao == "C":
  graus_kelvin = input("Informe os graus em kelvin para transformar em celcius: ")
  temperatura_celcius = float(graus_kelvin) + 273
  print("A temperatura em graus celcius é: ", temperatura_celcius)
else:
  if operacao == "K":
    graus_celcius = input("Informe os graus em celcius para transformar em kelvin: ")
    graus_kelvin = float(graus_celcius) - 273
    print("A temperatura em graus kelvin é: ", graus_kelvin)
  else:
    print("Operação invalida, informe (C ou K)")