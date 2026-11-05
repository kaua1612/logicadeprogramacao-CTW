#Construa um algoritmo que receba o código de vários produtos e os
#classifique de acordo com a tabela:
#CÓDIGO CLASSIFICAÇÃO
#1 Alimento não-perecível
#2 a 4 Alimento perecível
#5 e 6 Vestuário
#7 Higiene pessoal
#8 a 15 Limpeza e utensílios domésticos
#Qualquer outro código inválido exibe uma mensagem ao usuário.
#Quando o usuário digitar 0 (zero) o programa finaliza e exibe o número total
#de produtos classificados em cada categoria

qnt = 0
cod = 1

while cod != 0:
    cod = int(input("Digite o código do produto: "))
    

    if cod == 1 :
        print("O alimento não é perecível ")
        qnt = qnt + 1
        
    elif cod <=4 and cod >=2 :
        print("O alimento é perecível ")
        qnt = qnt + 1
    elif cod <=6 and cod >=5 :
        print("Vestúario ")
        qnt = qnt + 1
    elif cod ==7 :
        print("Higiene pessoal ")
        qnt = qnt + 1
    elif cod <= 15 and cod >=8 :
        print("Limpeza e utensílios domésticos ")
        qnt = qnt + 1
    else:
        print("Código invalido ")

    print("A quantidade total de produtos é: ",qnt)
    