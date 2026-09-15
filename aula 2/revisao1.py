# ---------------------------------------------
# Exercício 1: Fila prioritária
# Peça a idade da pessoa e se ela está gestante ou com
# alguma deficiência (sim/não). Se tiver mais de 60 anos,
# ou estiver gestante, ou tiver deficiência, ela tem direito
# a atendimento prioritário — imprima "Atendimento prioritário"
# ou "Fila normal", conforme o caso.
# ---------------------------------------------

idade = int(input("Digite a idade: "))
gestante = input("A pessoa está gestante? (sim/não): ")
deficiencia = input("A pessoa possui alguma deficiência? (sim/não): ")

if idade > 60 or gestante == "sim" or deficiencia == "sim":
    print("Atendimento prioritário")
else:
    print("Fila normal")