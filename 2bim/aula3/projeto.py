n1 = float(input("Digite o 1° numero: "))
n2 = float(input("Digite o 2° numero: "))
n3 = float(input("Digite o 3° numero: "))

if n1<=n2 and n1<=n3:
    print(f"Menor: {n1}")

elif n2<=n1 and n2<=n3:
    print(f"Menor: {n2}")

elif n3<=n2 and n3<=n1:
    print(f"Menor: {n3}")