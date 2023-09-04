#7

n = int(input("Informe a quantidade de notas: "))
contador = 1
soma = 0

while contador <= n:
    notas = float(input(f"Informe a {contador}° nota: "))
    soma = soma + notas
    contador = contador +1
media = soma/n
print(f"A média é {media:.2f}")