se = input("Digite seu sexo: ")
h = float(input("Digite sua altura: "))

if se=="masculino":
    idealh=(72.7*h)-58
    print(f"Seu peso ideal é {idealh}")

if se=="feminino":
    idealf=(62.1*h)-44.7
    print(f"Seu peso ideal é {idealf}")