#Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em um determinado dia. Para cada casa visitada foi fornecido o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo
#a ele naquela casa. Se a televisão estivesse desligada, nada seria anotado,
#ou seja, esta casa não entraria na pesquisa. Faça um Programa que:
#leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#calcule e imprima a porcentagem de audiência em cada canal. Para encerrar
#a entrada de dados, digite o número do canal zero.

totalPessoas4 = 0
totalPessoas5 = 0
totalPessoas7 = 0
totalPessoas12 = 0
total = 0 




while True:
    canal = int(input("Digite o número de um dos canais (4, 5, 7, 12): "))
    pessoas = int(input("Digite a quantidade de pessoas assistindo: "))


    if canal == 0:
        break
    elif canal != 4 and canal != 5 and canal !=7 and canal !=12: 
        print("Código inválido! ")
    elif canal == 4:
        totalPessoas4 += pessoas
    elif canal == 5:
        totalPessoas5 += pessoas
    elif canal == 7:
        totalPessoas7 += pessoas
    else:
        totalPessoas12 += pessoas 
    

total = totalPessoas4 + totalPessoas5 + totalPessoas7 + totalPessoas12



porcentagem4 = (totalPessoas4/total)*100
porcentagem5 = (totalPessoas5/total)*100
porcentagem7 = (totalPessoas7/total)*100
porcentagem12 = (totalPessoas12/total)*100


print("O percentual de pessoas do canal 4 é: " ,porcentagem4 )
print("O percentual de pessoas do canal 5 é: " ,porcentagem5 )
print("O percentual de pessoas do canal 7 é: " ,porcentagem7 )
print("O percentual de pessoas do canal 12 é: " ,porcentagem12 )

