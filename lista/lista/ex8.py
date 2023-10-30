qn = int(input("Digite a quantidade de notas: "))
lista = []

for i in range(qn):
    notas = float(input(f"Informe a {i}° nota: "))
    lista.append(notas)
    nota= nota+notas
print(notas/qn)