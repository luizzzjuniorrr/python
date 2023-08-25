quant = int(input("Digite quantas maças você comprou: "))

if quant>=12:
    total12= quant*0.25
    print(f"O total da compra deu: {total12}")

if quant<12:
    total11= quant*0.30
    print(f"O total da compra deu: {total11}")