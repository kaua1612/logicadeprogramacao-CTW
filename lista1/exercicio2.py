tabuada = int(input("Digite o numero da tabuada que deseja saber: "))
numero = int(input("Digite o numero: "))

for contador in range(1, numero +1):
    resultado = tabuada * contador
    print(tabuada,"X" , contador , "=" , resultado)