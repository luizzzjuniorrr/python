print("qual o seu salário?")
salario=float(input())
print("qual o valor da hora extra?")
extra=float(input())
print("quantas horas extras você trabalhou?")
hora=float(input())
valorhx=extra*hora
total=valorhx+salario
print("você ganhou", valorhx, "de horas extra e no total", total)