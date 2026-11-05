#Faça um algoritmo que leia vários códigos do jogador (1 ou 2) que ganhou o
#ponto em uma partida de pingue-pongue, e responda quem ganha a partida.
#A partida chega ao final se um dos jogadores chega a 21 pontos e a
#diferença de pontos entre os jogadores é maior ou igual a dois. Caso
#contrário, ganha aquele que, com mais de 21 pontos, consiga colocar uma
#vantagem de dois pontos sobre o adversário


pontJoga1 = 0
pontJoga2 = 0

while True:
    ponto = input("Digite quem fez o ponto (1 ou 2): ")

    if ponto == "1":
        pontJoga1 += 1
    elif ponto == "2":
        pontJoga2 += 1
    else:
        print("Digite apenas 1 ou 2!")
        continue

    print("Jogador 1:", pontJoga1)
    print("Jogador 2:", pontJoga2)

    if (pontJoga1 >= 21 and pontJoga1 - pontJoga2 >= 2) or (pontJoga2 >= 21 and pontJoga2 - pontJoga1 >= 2):
        break

if pontJoga1 > pontJoga2:
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")