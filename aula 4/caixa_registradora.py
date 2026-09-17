def registrar_compra(total_compra=0, quantidade_itens=0):
    produto = input("Digite o nome do produto (ou deixe em branco para finalizar): ").strip()

    if produto == "":
        print("----- RESUMO DA COMPRA -----")
        print(f"Quantidade total de itens: {quantidade_itens}")
        print(f"Total da compra: R$ {total_compra:.2f}")
        return

    quantidade = int(input(f"Digite a quantidade de '{produto}': "))
    preco = float(input(f"Digite o preço unitário de '{produto}': R$ "))

    subtotal = quantidade * preco
    print(f"{quantidade}x {produto} adicionado(s). Subtotal: R$ {subtotal:.2f}\n")

    registrar_compra(total_compra + subtotal, quantidade_itens + quantidade)


registrar_compra()
