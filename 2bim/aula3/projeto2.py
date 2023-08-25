m = float(input("Digite a quantidade de minutos: "))
if m>=100:
   print(f"Valor a pagar: {(m-100)*2.00+50}R$")
elif m<100:
    print(f"Valor a pagar: 50R$")                             