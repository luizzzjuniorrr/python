lista = []
s=0
m=0
na=0
for a in range(10):
    for i in range(4):

        n= float(input(f"Digite a {i+1}° nota do {a+1}° aluno: "))
        s=s+n
    m=s/10
    lista.append(m)
    if m >= 7:
        na+=1
    s=0
    m=0
print(f"O numero de alunos que alcançaram a meta foi: {na}")