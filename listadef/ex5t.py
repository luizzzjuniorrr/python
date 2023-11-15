def calcularimc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

if calcularimc(peso, altura) <= 18.5:
    print(f"IMC é classificado como: Abaixo do peso")
elif 18.5 <= calcularimc(peso, altura) <= 24.9:
    print(f"IMC é classificado como: Peso normal")
elif 25 <= calcularimc(peso, altura) <= 29.9:
    print(f"IMC é classificado como: Acima do peso(sobrepeso)")
elif 30 <= calcularimc(peso, altura) <= 34.9:
    print(f"IMC é classificado como: Obesidade I")
elif 35 <= calcularimc(peso, altura) <= 39.9:
    print(f"IMC é classificado como: Obesidade II")
elif calcularimc(peso, altura) >= 40:
    print(f"IMC é classificado como: Obesidade III")
