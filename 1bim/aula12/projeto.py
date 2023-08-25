vet = input("O animal é vertebrado ou invertebrado?: ")
tip = input("Qual a classe do animal?, mamifero, ave, inseto ou anelideo: ")
ali = input("O animal é, carnivoro, onivoro, herbivoro, hematofago, herbivoro ou hematofago: ")

if vet=="vertebrado" and tip=="ave" and ali=="carnivoro":
    print("Seu animal é uma aguia")
elif vet=="vertebrado" and tip=="ave" and ali=="onivoro":
    print("Seu animal é uma pomba")
elif vet=="vertebrado" and tip=="mamifero" and ali=="onivoro":
    print("Seu animal é um homem")
elif vet=="vertebrado" and tip=="mamifero" and ali=="herbivoro":
    print("Seu animal é uma vaca")
elif vet=="invertebrado" and tip=="inseto" and ali=="hematofago":
    print("Seu animal é uma pulga")
elif vet=="invertebrado" and tip=="inseto" and ali=="herbivoro":
    print("Seu animal é uma lagarta")
elif vet=="invertebrado" and tip=="anelideo" and ali=="hematofago":
    print("Seu animal é uma sanguesuga")
elif vet=="invertebrado" and tip=="inseto" and ali=="onivoro":
    print("Seu animal é uma minhoca")

else:
    print("O animal não foi identificado, porfavor verifique as suas respostas!")