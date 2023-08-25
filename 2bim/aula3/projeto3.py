gli = float(input("Digite o valor da glicose: "))

if gli<=100:
    print("Classificação: normal")

elif gli>100 and gli<=140:
    print("Classificação: elevado")

elif gli>140:
    print("Classificação: diabets")