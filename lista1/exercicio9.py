import random 
numMaquina = random.randint(1,50)
num = 0



for i in range(1,6):
    num = int(input("tente adivinhar o numero!: "))
    if num == numMaquina:
        print ("Você acertou o numero!")
        break
    elif num < numMaquina:
        print("número menor que o sorteado.")
    else:
        print("numero maior que o sorteado")

print("voce perdeu, o numero sorteado era: ",numMaquina )
        
