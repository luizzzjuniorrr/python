qn = int(input("Quantos numeros você deseja digitar?: "))
ndq=1
while ndq <= qn:
    n=int(input(f"Digite seu {ndq}° numero: "))
    ndq=ndq+1
md=n/ndq
print(md)