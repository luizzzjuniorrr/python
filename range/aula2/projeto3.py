t = int(input("Digite o numero para a tabuada: "))
s = int(input("Digite o numero de começo da tabuada: "))
e = int(input("Digite o numero final da tabuada: "))
if e<s:
        print(f"Numero final menor que numero inicial.")
else:
    for i in range(s,e+1):
        print(f"{i} x {t} = {t*i}")