peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso/(altura**2)

print("-------------------------")
print(f"O seu IMC é {imc:.2f}")
print("-------------------------")