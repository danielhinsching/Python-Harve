valor = float(input("Digite o valor do empréstimo: "))
meses = int(input("Digite em quantos meses será pago: "))
taxa = 0.03

parcela = valor / meses
juros_parcela = parcela * taxa
juros_total = juros_parcela * meses

valor_final = valor + juros_total

print("Valor da parcela (sem juros):", parcela)
print("Juros por parcela:", juros_parcela)
print("Juros total:", juros_total)
print("Valor final a pagar:", valor_final)