#Uma empresa utiliza os códigos 1 para funcionários do setor administrativo e 2 para os 
# funcionários do setor operacional. Faça um programa que receba o código e o salário de 20 funcionários. 
# Calcule e mostre:
# ●  A média salarial do setor administrativo.
# ●  A média salarial do setor operacional.
# ●  O total de salários pagos pela empresa.
# ●  A quantidade de funcionários em cada setor.


salarioADM = 0
salarioOP = 0
qtdADM = 0
qtdOP = 0

i = 0


while i < 20:
    cod = int(input(
        "(Cod 1 = funcionarios do setor ADM)\n"
        "(Cod 2 = funcionarios do setor operacional)\n"
        "Digite o codigo do funcionario: "
    ))

    if cod != 1 and cod != 2:
        print("Codigo invalido! Digite 1 ou 2.")
        continue

    elif cod == 1:
        salario = float(input("Digite o salario do funcionario: "))
        salarioADM += salario
        qtdADM += 1

    else:
        salario = float(input("Digite o salario do funcionario: "))
        salarioOP += salario
        qtdOP += 1

    i += 1

if qtdADM > 0:
    mediaADM = salarioADM / qtdADM
else:
    mediaADM = 0

if qtdOP > 0:
    mediaOP = salarioOP / qtdOP
else:
    mediaOP = 0

print("\n--- RESULTADO FINAL ---")
print("Total de salarios pagos pela empresa:", salarioADM + salarioOP)
print("Total de funcionarios do setor ADM:", qtdADM)
print("Total de funcionarios do setor operacional:", qtdOP)
print("Media salarial do setor ADM:", mediaADM)
print("Media salarial do setor operacional:", mediaOP)
