#2. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de 
#   números impares.

contador = 1

while contador <= 10:
    n1=int(input(f"Digite o {contador}° numero inteiro: "))
    contador=contador+1

    if n1 % 2==0:
        