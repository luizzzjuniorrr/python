par = 0
impar = 0

for i in range (1,11):
    num = int(input("Digite um numero inteiro: "))

    if num % 2==0:
        par+=1
    else:
        impar+=1
print(f"| Impar = {impar} |")
print(f"| Par   = {par} |")