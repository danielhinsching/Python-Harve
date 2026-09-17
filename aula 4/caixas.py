compratotal = {}
valortotal = 0
listaprodutos = []
def comprar(x, y, z):
      compratotal["Nome"] = x
      compratotal["Quantidade"] = y
      compratotal["Preço"] = z
      

for x in range(100):      
      nomeproduto = input("qual o nome do produto? ").strip()
      if nomeproduto == "":
            break
            print(f"os elementos da sua compra são: {compratotal} e o valor total é de {valortotal}")
      else:
            quantidadeproduto = int(input("qual a quantidade desse produto? "))
            precoproduto = float(input("qual o preço do produto? "))
            comprar(nomeproduto, quantidadeproduto, precoproduto)
            print(compratotal)      
      