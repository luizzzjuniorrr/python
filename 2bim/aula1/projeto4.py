b = float(input("Digite quanto mede a base lado do seu retangulo: (Em CM) "))
a = float(input("Digite quanto mede a altura lado do seu retangulo: (Em CM) "))

b2 = float(input("Digite quanto mede a base lado do seu segundo retangulo: (Em CM) "))
a2 = float(input("Digite quanto mede a altura lado do seu segundo retangulo: (Em CM) "))

area = b*a
area2 = b2*a2

if area==area2:
    print("A area dos retangulos são a mesma.")

else:
    print("A area dos retangulos são diferentes.")