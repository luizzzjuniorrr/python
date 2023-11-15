def valorparcela(valor):
    valorparcela = valor/vezes
    return valorparcela

valor = float(input("Qual o valor total da compra?: "))
vezes = int(input("Vai dividir em quantas vezes?: "))
print(f"Sua compra de R${valor} em {vezes}x de R${valorparcela(valor)} foi concluida!")