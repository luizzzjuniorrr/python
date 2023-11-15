
nota=0

def calcularmedia(nota):
    media = nota/3
    return media

for i in range(3):
    notas = float(input(f"Informe a {i+1}° nota: "))
    nota = nota+notas

faltas = int(input("Informe a quantidade de faltas: "))

if faltas >= 30:
    print(f"O aluno está: Reprovado por falta com a média: {calcularmedia(nota)}")

else:
    if calcularmedia(nota) >=8:
        print(f"O aluno está: Aprovado com sucesso com a média: {calcularmedia(nota)}")
    elif calcularmedia(nota) <=8 and calcularmedia(nota) >= 6:
        print(f"O aluno está: Aprovado com sucesso com a média: {calcularmedia(nota)}")
    elif calcularmedia(nota) <=5.9 and calcularmedia(nota) >= 3:
        print(f"O aluno está: De Recuperação com a média: {calcularmedia(nota)}")
    elif calcularmedia(nota) <=3:
        print(f"O aluno está: Reprovado com a média: {calcularmedia(nota)}")
    elif calcularmedia(nota) <=0:
        print(f"O aluno está: Desistente com a média: {calcularmedia(nota)}")