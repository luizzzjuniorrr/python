nota1 = float(input("Digite a nota do 1° bimestre: "))
nota2 = float(input("Digite a nota do 2° bimestre: "))
nota3 = float(input("Digite a nota do 3° bimestre: "))

todasn = (nota1+nota2+nota3)/3

if todasn>=6:
    print("Parabéns você foi aprovado!")
if todasn<=5:
    print("Você não foi aprovado :<")