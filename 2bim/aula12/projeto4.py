#10
contador = 1
cm= float(input(f"Produto {contador}: "))
soma = cm

while cm !=0:
    cm= float(input(f"Produto {contador}: "))
    contador=contador+1
    soma = soma + cm
print(f"Total: R${soma}")
vl= float(input("Dinheiro: R$"))
print(f"troco: R${soma-vl}")