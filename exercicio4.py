    #Uma loja utiliza o código 1 para transação à vista e 2 para transação a prazo. Faça um programa que receba o código e o valor de 15 transações.
#Calcule e mostre: 
#O valor total das compras à vista
#O valor total as compras a prazo
#O valor total das compras efetuadas
#O valor da primeira prestação das compras a prazo, sabendo se que essas serão pagas em três vezes


totalTranzacoes = 0
totalCompras = 0
totalDinheiro = 0
totalCartao = 0

while totalTranzacoes < 15:
    preco = float(input("Digite o valor a ser pago: "))

    pagamento = input(
        "Qual será a forma de pagamento?\n"
        "1 = dinheiro\n"
        "2 = cartão\n: "
    )

    if pagamento == "1":
        totalDinheiro += preco
        totalCompras += preco
        print("Você irá pagar:", preco)

    elif pagamento == "2":
        totalCartao += preco
        totalCompras += preco
        preco = preco / 3
        print("Você irá pagar 3x de", preco, "cada")

    else:
        print("Forma de pagamento inválida!")
        continue

    totalTranzacoes += 1

print("Total das compras à vista:", totalDinheiro)
print("Total das compras a prazo:", totalCartao)
print("Valor total das compras:", totalCompras)
print("Valor da primeira prestação:", totalCartao / 3)

