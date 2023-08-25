nivel = float(input("Digite o nivel: "))
pressao = float(input("Digite a pressão: "))
clima = input("Digite o clima: ")

if nivel==60000:
    if pressao<1500:
        if clima!="chuvoso":
            print("Iniciar o lançamento!")

        else:
            print("Aguardar a chuva passar")
        
    else:
        print("Problema na pressão atmosferica")

else:
    print("Problema com o nivel de combustivel")