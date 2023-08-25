n1 = float(input("Digite a nota do 1° bim: "))
n2 = float(input("Digite a nota do 2° bim: "))
n3 = float(input("Digite a nota do 3° bim: "))
n4 = float(input("Digite a nota do 4° bim: "))
n5 = float(input("Digite a nota do 5° bim: "))

nf = (n1+n2+n3+n4+n5)/5

if nf>=6:
    print("Você foi aprovado!")

else:
    print("Você foi reprovado!")