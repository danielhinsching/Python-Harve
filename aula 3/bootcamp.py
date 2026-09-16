for x in range(100):
    numero1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    numero2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            print("Erro: divisão por zero.")
            continue
        resultado = numero1 / numero2
    else:
        print("Operação inválida.")
        continue

    print(f"Resultado: {resultado}")

    resposta = input("Deseja continuar? (s/n): ").strip().lower()
    if resposta != "s":
        break
