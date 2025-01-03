def sudoku(sudoku: list[int]):
    numeros = {}
    for i in range(1,10):
        numeros[str(i)] = 0

    # verifica linha
    for linha in sudoku:
        linha = str(linha)
        linha = list(linha)

        for num in linha:
            numeros[num] += 1

        for i in range(1,10):
            if numeros[str(i)] != 1:
                return False
            numeros[str(i)] = 0
    # verifica linha

    # verifica coluna
    for index,linha in enumerate(sudoku):
        sudoku[index] = str(linha)


    for linha in range(len(sudoku)):

        for col in range(9):
            numeros[sudoku[col][linha]] += 1

        for i in range(1,10):
            if numeros[str(i)] != 1:
                return False
            numeros[str(i)] = 0
    # verifica coluna

    # verifica quadrado 3x3
    quadrados3x3 = []
    for socorro in range(0,len(sudoku),3):
        for quadrado in range(0,len(sudoku),3):
            quadrado3x3 = []
            for i in range(socorro,socorro+3):
                for j in range(quadrado,quadrado+3):
                    quadrado3x3.append(sudoku[i][j])
            quadrados3x3.append("".join(quadrado3x3))

    for quadrado in quadrados3x3:
        for num in quadrado:
            numeros[num] += 1

        for i in range(1,10):
            if numeros[str(i)] != 1:
                return False
            numeros[str(i)] = 0
            
    # verifica quadrado 3x3

    return True