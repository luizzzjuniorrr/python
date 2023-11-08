qn= int(input("Informe a quantidade de numeros a serem digitados: "))
lista = []
listap = []
listai = []

for i in range(qn):
    n = int(input(f"Informe o {i+1}° numero: "))
    lista.append(n)

    if n % 2==0:
        listap.append(n)
    else:
        listai.append(n)
print(f"Numeros informados: {lista}")
print(f"Numeros pares {listap}")
print(f"Numeros impares {listai}")