#Uma sequência de 50 números será informada pelo usuário. Escreva um programa que:
# ●     Conte quantos desses números são múltiplos de 3.
# ●     Exiba a soma de todos os números pare


for i in range(50)
    numero = int(input("Digite um numero: "))

    if numero%3 == 0:
        mulTres += 1 
    if numero%2 == 0:
        somaPares += numero

print("Soma dos numeros multiplos de três: "mulTres)
print("A soma dos numeros pares: ",somaPares)

