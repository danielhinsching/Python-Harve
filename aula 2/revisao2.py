# ---------------------------------------------
# Exercício 2: Verificador de convidados
# Dada a lista convidados = ["Ana", "Bruno", "Carla", "Diego"],
# peça ao usuário o nome de uma pessoa. Use if/else com o
# operador in pra verificar: se o nome ESTIVER na lista,
# imprima "Já confirmado" e remova o nome da lista (remove);
# se NÃO estiver, adicione o nome à lista (append) e imprima
# "Confirmação adicionada". No final, exiba a lista atualizada.
# ---------------------------------------------

convidados = ["Ana", "Bruno", "Carla", "Diego"]
nome = input("Digite o nome do convidado: ")

if nome in convidados:
    print("Já confirmado")
    convidados.remove(nome)
else:
    print("Confirmação adicionada")
    convidados.append(nome)

print(convidados)