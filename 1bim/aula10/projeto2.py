pnumero = float(input("Digite o primeiro numero: "))
op = input("Digite o tipo de operação: ")
snumero = float(input("Digite o segundo numero: "))

if op=="+":
    print(f"O resultado é igual a {pnumero+snumero:.2f}")

elif op=="-":
    print(f"O resultado é igual a {pnumero-snumero:.2f}")

elif op=="/":
    print(f"O resultado é igual a {pnumero/snumero:.2f}")

elif op=="*":
    print(f"O resultado é igual a {pnumero*snumero:.2f}")