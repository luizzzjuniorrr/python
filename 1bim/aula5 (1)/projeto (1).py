validos = int(input("Digite o numero de votos válidos:"))
nulos = int(input("Digite o numero de votos nulos:"))
brancos = int(input("Digite o numero de votos brancos:"))

total = validos+nulos+brancos

pvalidos = (validos/total)*100
pnulos = (nulos/total)*100
pbrancos = (brancos/total)*100
ptotal = (total/total)*100

print("-----------------------------")
print("Votos válidos   = ", validos, "(", pvalidos, ")")
print("Votos nulos   = ", nulos, "(", pnulos, ")")
print("Votos brancos   = ", brancos, "(", pbrancos, ")")
print("Total de votos = ", total, "(", ptotal, ")")