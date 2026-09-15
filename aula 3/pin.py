def jogo_do_pin(multiplo, limite):
    contagem = []
    for numero in range(1, limite + 1):
        if numero % multiplo == 0:
            contagem.append("pin")
        else:
            contagem.append(str(numero))
    return ", ".join(contagem)


multiplo = int(input("Digite o múltiplo do jogo do pin: "))
limite = int(input("Digite o limite da contagem: "))

print(jogo_do_pin(multiplo, limite))
