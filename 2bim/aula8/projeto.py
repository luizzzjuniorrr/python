#1

n = int(input("Digite um numero inteiro: "))
n1 = int(input("Digite um segundo numero inteiro: "))

if n1 <= n:
    while n1 <= n:
        print(f"{n1}")
        n1=n1+1
elif n <= n1:
    while n <= n1:
        print(f"{n}")
        n=n+1