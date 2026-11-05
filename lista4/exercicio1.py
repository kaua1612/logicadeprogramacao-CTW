
meta = int(input("Qual é a meta diária?: "))
capMx = int(input("Qual é a capacidade máxima por estação?: "))

producaoTotal = 0
ciclos = 0

c90 = capMx * 0.9

pecas1 = 0
pecas2 = 0
pecas3 = 0
pecas4 = 0
pecas5 = 0

c901 = 0
c902 = 0
c903 = 0
c904 = 0
c905 = 0

estacaoFalhou = 0

while producaoTotal < meta and estacaoFalhou == 0:
    ciclos = ciclos + 1

    entrada = int(input("Quantas peças entraram: "))
    pecas1 = pecas1 + entrada

    # Estação 1
    if pecas1 > capMx:
        processadas1 = capMx
    else:
        processadas1 = pecas1

    pecas1 = pecas1 - processadas1

    if processadas1 > c90:
        c901 = c901 + 1
    else:
        c901 = 0

    if c901 >= 5:
        estacaoFalhou = 1

    # Estação 2
    if estacaoFalhou == 0:
        pecas2 = pecas2 + processadas1

        if pecas2 > capMx:
            processadas2 = capMx
        else:
            processadas2 = pecas2

        pecas2 = pecas2 - processadas2

        if processadas2 > c90:
            c902 = c902 + 1
        else:
            c902 = 0

        if c902 >= 5:
            estacaoFalhou = 2

    # Estação 3
    if estacaoFalhou == 0:
        pecas3 = pecas3 + processadas2

        if pecas3 > capMx:
            processadas3 = capMx
        else:
            processadas3 = pecas3

        pecas3 = pecas3 - processadas3

        if processadas3 > c90:
            c903 = c903 + 1
        else:
            c903 = 0

        if c903 >= 5:
            estacaoFalhou = 3

    # Estação 4
    if estacaoFalhou == 0:
        pecas4 = pecas4 + processadas3

        if pecas4 > capMx:
            processadas4 = capMx
        else:
            processadas4 = pecas4

        pecas4 = pecas4 - processadas4

        if processadas4 > c90:
            c904 = c904 + 1
        else:
            c904 = 0

        if c904 >= 5:
            estacaoFalhou = 4

    # Estação 5
    if estacaoFalhou == 0:
        pecas5 = pecas5 + processadas4

        if pecas5 > capMx:
            processadas5 = capMx
        else:
            processadas5 = pecas5

        pecas5 = pecas5 - processadas5

        if processadas5 > c90:
            c905 = c905 + 1
        else:
            c905 = 0

        if c905 >= 5:
            estacaoFalhou = 5

        producaoTotal = producaoTotal + processadas5

print("Produção total:", producaoTotal)
print("Ciclos executados:", ciclos)

if estacaoFalhou == 0:
    print("Nenhuma estação falhou.")
else:
    print("Estação que falhou:", estacaoFalhou)
