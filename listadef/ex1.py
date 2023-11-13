def total(x):
    total = salario+(x*(tb/100))-desconto
    return total

salario= float(input("Salário: "))
tb= float(input("Bonus: "))
desconto = float(input("Desconto: "))
print(f"Salário liquido: {total(total)}")   