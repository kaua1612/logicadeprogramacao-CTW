#Faça uma Programa que receba, como entrada, uma lista de números
#positivos ou negativos finalizada com o número zero e forneça, como saída, a
#soma dos números positivos, a soma dos números negativos e a soma das
#duas somas parciais e mostre os números pares e ímpares ao final.

positivo =0
negativo =0




while True:
    num = float(input("digite um numero: "))

    if num > 0:
        positivo += num


    elif num < 0:
        negativo += num


    else:



        print("A soma dos numeros positivos é: ",positivo)
        print("A soma dos numeros negativos é: ",negativo)
        print("A diferença entre os numeros positivos e negativos é: " , positivo - negativo)
        break

