sa = float(input("Digite seu salário: "))

if sa>=0 and sa<=280:
    print(f"Seu salario anterior era R${sa}")
    print("O aumento foi de 20%")
    print(f"O valor de aumento foi {sa*0.2}")
    print(f"O seu salario atual é de R$ {sa*0.2+sa}")

elif sa>=281 and sa<=700:
    print(f"Seu salario anterior era R${sa}")
    print("O aumento foi de 15%")
    print(f"O valor de aumento foi {sa*0.15}")
    print(f"O seu salario atual é de R$ {sa*0.15+sa}")

elif sa>=701 and sa<=1500:
    print(f"Seu salario anterior era R${sa}")
    print("O aumento foi de 10%")
    print(f"O valor de aumento foi {sa*0.1}")
    print(f"O seu salario atual é de R$ {sa*0.1+sa}")

elif sa>=1501:
    print(f"Seu salario anterior era R${sa}")
    print("O aumento foi de 5%")
    print(f"O valor de aumento foi {sa*0.05}")
    print(f"O seu salario atual é de R$ {sa*0.05+sa}")
