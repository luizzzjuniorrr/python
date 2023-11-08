qn = int(input("Informe a quantidade de numeros da lista: "))
lista = []
sm=0
mul=1

for i in range(qn):
    n = int(input(f"Informe o {i+1}° numero: "))
    lista.append(n)
    sm+=n
    mul= mul*n

print(f"A lista é: {lista}")
print(f"A soma é {sm}")
print(f"A multiplicação é {mul}")