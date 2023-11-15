def calcularimc(altura):
    imc = peso/(altura**2)
    return imc

altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

if calcularimc(altura) <=18.5:
        print(f"IMC é classificado como: Abaixo do peso")
elif calcularimc(altura) >=18.5 and calcularimc(altura) <= 24.9:
        print(f"IMC é classificado como: Peso normal")
elif calcularimc(altura) >=25 and calcularimc(altura) <= 29.9:
        print(f"IMC é classificado como: Acima do peso(sobrepeso)")
elif calcularimc(altura) >=30 and calcularimc(altura) <= 34.9:
        print(f"IMC é classificado como: Obesidade I")
elif calcularimc(altura) >=35 and calcularimc(altura) <= 39.9:
        print(f"IMC é classificado como: Obesidade II")
elif calcularimc(altura) >=40:
        print(f"IMC é classificado como: Obesidade III")