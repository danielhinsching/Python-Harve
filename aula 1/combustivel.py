distancia = input("Qual a distância em km? ")
consumo = input("Qual o consumo do carro em km/l? ")
distancia = float(distancia)
consumo = float(consumo)
litros_necessarios = distancia / consumo
print("Serão necessários", litros_necessarios, "litros de combustível.")