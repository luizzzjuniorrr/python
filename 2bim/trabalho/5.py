na= int(input("Informe um numero natural par: "))

while na >= 0:
    if na % 2==0:
        print(na)
        na-=2
    else:
        na=na -1
        