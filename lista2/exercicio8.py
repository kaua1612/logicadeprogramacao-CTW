#Faça um programa que receba o valor de um carro e mostre uma tabela com
#os seguintes dados: preço final, quantidade de parcelas e valor da parcela.
#Considere o seguinte:
#● O preço final para compra à vista tem um desconto de 20%;
#● A quantidades de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.
# Os percentuais de acréscimo seguem a tabela a seguir.


valorCarro = float(input("Digite o valor do carro base: "))
valorFinalDesconto = valorCarro - (valorCarro*0.2)


valor6vezes= valorCarro+(valorCarro*0.3)
valor12vezes= valorCarro+(valorCarro*0.6)
valor18vezes= valorCarro+(valorCarro*0.9)
valor24vezes= valorCarro+(valorCarro*1.2)
valor30vezes= valorCarro+(valorCarro*1.5)
valor36vezes= valorCarro+(valorCarro*1.8)
valor42vezes= valorCarro+(valorCarro*2.1)
valor48vezes= valorCarro+(valorCarro*2.4)
valor54vezes= valorCarro+(valorCarro*2.7)
valor60vezes= valorCarro+(valorCarro*3.0)

valorParcelas6 = valor6vezes/6
valorParcelas12 = valor12vezes/12
valorParcelas18 = valor18vezes/18
valorParcelas24 = valor24vezes/24
valorParcelas30 = valor30vezes/30
valorParcelas36 = valor36vezes/36
valorParcelas42 = valor42vezes/42
valorParcelas48 = valor48vezes/48
valorParcelas54 = valor54vezes/54
valorParcelas60 = valor60vezes/60


print("O valor do carro a vista é: ",valorFinalDesconto)
print("---------------------------------------------------------------------------")
print("O valor do carro com o juros das parcelas: ",valor6vezes)
print("O valor do carro com o juros das parcelas: ",valor12vezes)
print("O valor do carro com o juros das parcelas: ",valor18vezes)
print("O valor do carro com o juros das parcelas: ",valor24vezes)
print("O valor do carro com o juros das parcelas: ",valor30vezes)
print("O valor do carro com o juros das parcelas: ",valor36vezes)
print("O valor do carro com o juros das parcelas: ",valor42vezes)
print("O valor do carro com o juros das parcelas: ",valor48vezes)
print("O valor do carro com o juros das parcelas: ",valor54vezes)
print("O valor do carro com o juros das parcelas: ",valor60vezes)
print("---------------------------------------------------------------------------")
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor6vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor12vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor18vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor24vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor30vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor36vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor42vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor48vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor54vezes)
print("O valor de cada parcela, parcelado em 6 vezes é: ",valor60vezes)