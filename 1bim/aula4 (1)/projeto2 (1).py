salh = float(input("Quanto você recebe por hora?: R$"))
qnth = float(input("Quantas horas você trabalhou este mês?"))

salbru = salh*qnth

salbrut = salbru*(11/100)
inss = salbru*(8/100)
sindicato = salbru*(5/100)

liq = salbru-(inss+sindicato+salbrut)

print("+ Salário bruto =", salbru, "$")
print("- IR (11%) =", salbrut, "$")
print("- INSS (8%) =", inss, "$")
print("- Sindicato (5%)", sindicato, "$")
print("+ Salário líquido =", liq, "$")