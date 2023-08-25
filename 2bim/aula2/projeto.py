ns1= float(input("Digite a nota do primeiro semestre: "))
ns2= float(input("Digite a nota do segundo semestre: "))

nf = ns1+ns2

if nf>=60:
    print(f"NOTA FINAL = {nf:.1f}")
else:
    print(f"NOTA FINAL = {nf:.1f}")
    print("REPROVADO")