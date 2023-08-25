aatual = int(input("Digite o ano atual: "))
anasci = int(input("Digite o ano que você nasceu: "))

idade = aatual-anasci

if idade>=16:
    print("-----------------------------------------------------------------------")
    print(f"Você possui {idade} anos e já pode votar;")
    print("-----------------------------------------------------------------------")

if idade<16:
    print("-----------------------------------------------------------------------")
    print(f"Você possui {idade} anos e não pode votar;")
    print("-----------------------------------------------------------------------")

if idade>=18:
    print(f"Você possui {idade} anos e já pode tirar carteira de habilitação;")
    print("-----------------------------------------------------------------------")

if idade<18:
    print(f"Você possui {idade} anos e não pode tirar carteira de habilitação;")
    print("-----------------------------------------------------------------------")