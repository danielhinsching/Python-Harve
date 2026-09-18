# Vamos fazer o programa que faria você ficar rico no programa Silvio Santos. Um algoritmo que solucione sempre o jogo do pin. Para entender o jogo, iremos inserir um múltiplo e o limite e dentro desses parâmetros, faremos o programa imprimir a contagem de acordo com o pin. Nela, devemos contar 1,2,3... até o limite. Porém, quando chegar no número múltiplo, devemos dizer pin ao invés do número e continuar a contagem. Quando chegar novamente no múltiplo, o raciocínio se repete.



def jogo_do_pin(x, y):
    contagem = []
    for numero in range(1, y + 1):
        if numero % x == 0:
            contagem.append("pin")
        else:
            contagem.append(str(numero))
    return ", ".join(contagem)


multiplo = int(input("Digite o múltiplo do jogo do pin: "))
limite = int(input("Digite o limite da contagem: "))

print(jogo_do_pin(multiplo, limite))
