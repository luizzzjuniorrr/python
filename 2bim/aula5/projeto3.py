#ex13
#1) Opção: a vista com 10% de desconto
#2) Opção: em 2 vezes sem juros
#3) Opção: de 3 até 10 vezes com 3% de juros ao mês (somente para compras acima de R$100,00).

valor = float(input("Digite o valor gasto: "))
print("1) À vista.")
print("2) Dividir em 2 vezes.")
print("3) Dividir de 3 a 10 vezes.")

fp = int(input("Selecione a forma de pagamento: "))

if fp == 1:
    print(f"Valor a pagar: R${valor:.2f}")

if fp == 2:
    print(f"Valor a pagar R${valor:.2f}, pagos em 2 vezes de R${valor/2:.2f}")

if fp == 3:
    pc = float(input("Informe o número de parcelas: "))
    print(f"Valor a pagar R${valor:.2f}, pagos em {pc:.1f} vezes de R${(valor/pc)+(valor*0.03):.2f}")