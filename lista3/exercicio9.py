#Um professor registrou as notas de 35 alunos em uma prova. Faça um algoritmo que:
# ●     Leia o nome e a nota de cada aluno.
# ●     Informe a média geral da turma.
# ●     Conte quantos alunos tiveram nota acima de 7.

i = 0
a7 = 0
notaG = 0

while i <= 35:
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    notaG += nota
    mediaG = notaG / 35
    i += 1

    if nota > 7:
        a7 += 1 

print("Media turma é: ",mediaG)
print("A quantidade de alunos com nota acima de 7 é: ",a7)
    





