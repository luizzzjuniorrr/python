nm = input("Informe o nome do(a) atleta: ")
lista = []
st=0

for i in range(5):
    s = float(input(f"Informe o {i+1}° salto: "))
    lista.append(s)
    st+=s
print(f"Atleta: {nm}")
print(f"Saltos: {lista}")
print(f"A média dos saltos: {st/5}m")