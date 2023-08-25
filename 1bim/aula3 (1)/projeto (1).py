nome=input("Digite seu nome:")
idade=int(input("Digite sua idade:"))
disc=input("Digite a disciplina:")
nota1=float(input("Digite a nota da prova 1:"))
nota2=float(input("Digite a nota da prova 2:"))
nota3=float(input("Digite a nota da prova 3:"))
nota4=float(input("Digite a nota da prova 4:"))

f1 = nota1+nota2+nota3+nota4
f2 = f1 / 4

print("-------------------------------------")
print("Nome:", nome, "| Idade:", idade, "| Disciplina:", disc)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Nota 4:", nota4)
print("Media final:",f2)