def velocidade_media(distancia, tempo):
    return distancia / tempo


distancia = float(input("Digite a distância percorrida (km): "))
tempo = float(input("Digite o tempo da viagem (horas): "))

print(f"A velocidade média foi de {velocidade_media(distancia, tempo)} km/h")
