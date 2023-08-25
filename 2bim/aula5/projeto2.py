# ex12

pp = float(input("Digite o valor do seu produto: "))
qnt = float(input("Digite a quantidade comprada: "))
dr = float(input("Digite o valor recebido: "))
valort = dr-(pp*qnt)

if dr < valort:
    print(f"TROCO: {dr-(pp*qnt)}")

else:
    print(f"DINHEIRO INSUFICIENTE FALTA: {valort-dr}")