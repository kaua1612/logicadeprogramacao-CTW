#João tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
#metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e
#imprima quantos anos serão necessários para que Zé seja maior que João.


altJoao = 150
altZe = 110
ano = 0 



while altZe < altJoao:
    ano = ano + 1
    altZe = ano * 3 + altZe
    altJoao = ano * 2 + altJoao 

    if altZe > altJoao:
        print("Zé demorou ",ano," anos para passar Joao.")


