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




# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
