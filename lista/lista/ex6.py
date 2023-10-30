quantidade = int(input("Informe a quantidade de números na lista: "))
lista = []
for i in range(quantidade):
    n = int(input(f"Informe o número de índice {i+1} da lista: "))
    n2 = n*2
    lista.append(n2)
print(lista)