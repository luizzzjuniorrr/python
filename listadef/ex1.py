def total(salario):
    total = salario+(salario*(bonus/100))-desconto
    return total

salario = float(input("Salário: "))
bonus = float(input("Bônus: "))
desconto = float(input("Desconto: "))

print(f"Salário líquido: R$ {total(salario)}")