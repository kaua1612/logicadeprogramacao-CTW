#Solicite ao usuário um número inteiro n e exiba uma estrutura em forma de triângulo numérico de tamanho n. 
#Cada linha do triângulo deve conter números de 1 até o número da linha.



num = int(input("Digite um numero inteiro: "))

for i in range(1, num + 1):
    linha = ""
    for j in range(1, i + 1):
        linha = linha + str(j)
    print(linha)