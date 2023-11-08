qn = int(input("Digite a quantidade de notas: "))
lista = []
nota=0

for i in range(qn):
    notas = float(input(f"Informe a {i+1}° nota: "))
    lista.append(notas)
    nota = nota + notas
print(nota/qn)