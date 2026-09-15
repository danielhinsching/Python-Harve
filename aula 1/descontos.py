preco_original = input("Qual o preço original do produto? ")
preco_original = float(preco_original)
desconto = input("desconto(de 0 a 100):")
desconto = int(desconto)
calculo = (preco_original * desconto) / 100
valor_final = preco_original - calculo

print("valor com desconto:", valor_final)