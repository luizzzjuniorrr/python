inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
lista = []

for elementos in range(fim,inicio-1,-1):
    lista.append(elementos)
print(lista)