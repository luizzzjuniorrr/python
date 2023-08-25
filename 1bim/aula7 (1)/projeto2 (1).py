raio = float(input("Digite o raio do primeiro tanque: "))
altura = float(input("Digite a altura do primeiro tanque: "))
raio2 = float(input("Digite o raio do segundo tanque: "))
altura2 = float(input("Digite a altura do segundo tanque: "))
area1= 2*3.14*raio*(raio+altura)
area2= 2*3.14*raio2*(raio2+altura2)
areat = area1+area2

print("----------------------------------------------------------------------------")
print(f"Para pintar a área total de {areat:.2f}m² custará R$ {areat*115.75:.2f}")
print("----------------------------------------------------------------------------")