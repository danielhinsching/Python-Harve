nota1 = input("quanto voce tirou na primeira prova (0 - 10)?")
nota1 = float(nota1)
nota2 = input("quanto voce tirou na segunda prova (0 - 10)?")
nota2 = float(nota2)

resultado = nota1 * 0.6 + nota2 * 0.4
print("sua nota final é:", round(resultado,1))