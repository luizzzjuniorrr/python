#2

contador = 1
impar = 0
par = 0


while contador <= 10:
    n1=int(input(f"Digite o {contador}° numero inteiro: "))
    contador=contador+1
    if n1%2==0:
        par=par+1
    elif n1%2!=0:
        impar=impar+1
print(f"Impar: {impar}")
print(f"Par: {impar}")