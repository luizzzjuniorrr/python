na= int(input("Informe um numero natural: "))

while na >= 0:
    if na % 3==0:
        print(na)
        na-=2
    else:
        na=na -1
        