#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
#Calcule e mostre o valor a ser pago por item (preço *quantidade) e o total geral do pedido. 
#Considere que o cliente deve informar quando o pedido deve ser encerrado.
#Especificação      Código     Preço
#Cachorro Quente     100      R$ 1,20
#Bauru Simples       101      R$ 1,30
#Bauru com ovo       102      R$ 1,50
#Hambúrguer          103      R$ 1,20
#Cheeseburguer       104      R$ 1,30
# Refrigerante        105      R$ 1,00

totalGeral = 0
precoC = 0 
precoBS = 0
precoBO = 0
precoH = 0
precoCH = 0
precoRefri = 0  

while True:
    codigo = int(input("Digite o código do lanche (0 para encerrar): "))
   
    if codigo == 0:
        print("O valor total a ser pago é de:",totalGeral)
        break
    qnt = int(input("Digite a quantidade que você deseja: "))
    if codigo == 100:
        print("Você escolheu cachorro quente!")
        precoC = 1.20 * qnt
        print("O valor a ser pago é de: ",precoC)
        totalGeral += precoC
    elif codigo == 101:
        print("Você escolheu Bauru Simples! ")
        precoBS = 1.30 * qnt
        print("O valor a ser pago é de: ",precoBS)
        totalGeral += precoBS
    elif codigo == 102:
        print("Você escolheu Bauru com ovo!")
        precoBO = 1.50 * qnt
        print("O valor a ser pago é de: ",precoBO)
        totalGeral += precoBO
    elif codigo == 103:
        print("Você escolheu Hambúrguer!")
        precoH = 1.20 * qnt
        print("O valor a ser pago é de: ",precoH)
        totalGeral += precoH
    elif codigo == 104:
        print("Você escolheu Cheeseburguer!")-
        precoH = 1.30 * qnt
        print("O valor a ser pago é de: ",precoCH)
        totalGeral += precoCH
    elif codigo == 105:
        print("Você escolheu refrigerante!")
        precoH = 1.00 * qnt
        print("O valor a ser pago é de: ",precoRefri)
        totalGeral += precoRefri
        
    


