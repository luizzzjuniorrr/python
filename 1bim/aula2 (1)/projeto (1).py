print("Digite o preço do produto 1:")
p1 = float(input())
print("Digite a quantidade do produto 1:")
q1 = int(input())
print("")
print("Digite o preço do produto 2:")
p2 = float(input())
print("Digita a quantidade do produto 2:")
q2 = int(input())
print("")

total1= q1*p1
total2= q2*p2

print("----------------------")
print("SUBTOTAL")
print(q1, "X R$", p1, "= R$", total1)
print(q2, "X R$", p2, "= R$", total2)
print("----------------------")
print("")
print("total = R$",total1+total2)