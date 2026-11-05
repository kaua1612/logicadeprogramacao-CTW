#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida
# valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Qtd parcelas	% Juros sobre o valor inicial da dívida
# 1	                0
# 3	                10
# 6 	            15
# 9 	            20
# 12	            25

valorDiv = float(input("Digite o valor da sua divida: "))

print("TABELA DE JUROS: "
"Qtd parcelas"  "Juros em %"
    "\n1                      0"
    "\n3                      10"
    "\n6                      15"
    "\n9                      20"
    "\n12                     25"  
)
qnt = int(input("Digite a quantidade de parcelas: "))
    
if qnt == 1:
    print("O valor da sua divida é de: ",valorDiv)
    print("seu valor dos juros é de: 0")
    print("A sua quantidade de parcelas é 1x e o seu valor de cada parcela é de: ",valorDiv)

elif qnt == 3:
    valorF = float
    print("O valor da sua divida é de: ",valorDiv)
    valorF = valorDiv * 1.1
    valorJ = valorF - valorDiv
    print("O valor dos juros é de: ",valorJ)
    valorP3 = valorF / 3
    print("A sua quantidade de parcelas é 3x e o seu valor de parcela é de: ",valorP3)

elif qnt == 6:
    valorF = float
    print("O valor da sua divida é de: ",valorDiv)
    valorF = valorDiv * 1.15
    valorJ = valorF - valorDiv
    print("O valor dos juros é de: ",valorJ)
    valorP6 = valorF / 6
    print("A sua quantidade de parcelas é 3x e o seu valor de parcela é de: ",valorP6)

elif qnt == 9:
    valorF = float
    print("O valor da sua divida é de: ",valorDiv)
    valorF = valorDiv * 1.20
    valorJ = valorF - valorDiv
    print("O valor dos juros é de: ",valorJ)
    valorP9 = valorF / 9
    print("A sua quantidade de parcelas é 3x e o seu valor de parcela é de: ",valorP9)

elif qnt == 12:
    valorF = float
    print("O valor da sua divida é de: ",valorDiv)
    valorF = valorDiv * 1.25
    valorJ = valorF - valorDiv
    print("O valor dos juros é de: ",valorJ)
    valorP12 = valorF / 12
    print("A sua quantidade de parcelas é 3x e o seu valor de parcela é de: ",valorP12)

