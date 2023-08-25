ca = float(input("Digite seu coeficiente a: "))          
cb = float(input("Digite seu coeficiente b: "))
cc = float(input("Digite seu coeficiente c: "))

d= (cb**2)-(4*ca*cc)

if d < 0:
    print("Esta equação não possui raizes reais")

else:
    x1 = (-cb+(d**0.5))/(2*ca)
    x2 = (-cb-(d**0.5))/(2*ca)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")