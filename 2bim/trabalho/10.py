n1 = int(input("somar impares de 1 até: "))
n=n1
nf=n1

if n1%2==0:
    n1=n1-1
    while 1 <= n1:
        nf=n1+2
        print(f"impares de 1 até {n} = {nf}")

else:
    while 1 <= n1:
        nf=n1+2
        print(f"impares de 1 até {n} = {nf}")