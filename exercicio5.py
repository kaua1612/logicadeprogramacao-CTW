#Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#ótimo=3, bom=2, regular=1. Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre: (2 pontos)
#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados

qntBom = 0
qntRegular = 0
totalPessoas = 0
somaIdades = 0
totalOtimo = 0

while totalPessoas < 15:
    idade = int(input("Digite a sua idade: "))

    nota = input(
        "Digite a sua nota para o filme:\n"
        "3 = Ótimo\n"
        "2 = Bom\n"
        "1 = Regular\n"
        ": "
    )

    if nota == "3":
        somaIdades += idade
        totalOtimo += 1

    if nota == "1":
        qntRegular += 1

    totalPessoas += 1

    if nota == "2": 
        qntBom += 1 

if totalOtimo > 0:
    media = somaIdades / totalOtimo
    print("A média das idades de quem respondeu Ótimo foi:", media)
else:
    print("Ninguém respondeu Ótimo.")

porcentagem = (qntBom / totalPessoas) * 100

print("A porcentagem de pessoas que responderam Bom foi:", porcentagem, "%")

print("A quantidade de pessoas que responderam Regular foi:", qntRegular)



