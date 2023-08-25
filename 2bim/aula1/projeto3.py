q = float(input("Digite quanto mede um lado do seu quadrado: (Em CM) "))

q2 = float(input("Digite quanto mede um lado do seu segundo quadrado: (Em CM) "))

area = q*q
area2 = q2*q2

if area==area2:
    print("A area dos quadrados são a mesma.")

else:
    print("A area dos quadrados são diferentes.")