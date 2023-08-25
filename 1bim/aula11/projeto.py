peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = (peso / (altura**2))

if imc<=18.5:
    print(f"Seu IMC é {imc:.2f}, Você está abaixo do peso.")

elif imc<=25:
    print(f"Seu IMC é {imc:.2f}, você está no seu peso normal")

elif imc<=30:
    print(f"Seu IMC é {imc:.2f}, você está acima do seu peso ideal.")

elif imc>30:
    print(f"Seu IMC é {imc:.2f}, você está obeso;")