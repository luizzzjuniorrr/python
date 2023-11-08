print("Operação de adição")
lista = []

a = float(input("Informe um numero: "))
b= float(input("Informe outro numero: "))
soma=a+b
lista.append(soma)
realizar = input("Deseja realizar outra adição? [S ou N]: ")

while realizar == "S":
    a = float(input("Informe um numero: "))
    b= float(input("Informe outro numero: "))
    soma=a+b
    lista.append(soma)
    realizar = input("Deseja realizar outra adição? [S ou N]: ")
