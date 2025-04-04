function len(x) {
    return x.length()
}
function sudoku(sudoku) {
    let numeros = {}
    for (let i = 1;i < 10;i++) {
        numeros[String(i)] = 0
    }

    // verifica linha
    for (let linha in sudoku) {
        linha = String(linha)
        linha = list(linha)

        for (let num in linha) {
            numeros[num] += 1
        }

        for (let i = 1;i < 10;i++) {
            if (numeros[String(i)] !== 1) {
                return false
            }
            numeros[String(i)] = 0
        }
    }
    // verifica linha

    // verifica coluna
    for (let index,linha in enumerate(sudoku)) {
        sudoku[index] = String(linha)
    }


    for (let linha = 0;linha < len(sudoku);linha++) {

        for (let col = 0;col < 9;col++) {
            numeros[sudoku[col][linha]] += 1
        }

        for (let i = 1;i < 10;i++) {
            if (numeros[String(i)] !== 1) {
                return false
            }
            numeros[String(i)] = 0
        }
    }
    // verifica coluna

    // verifica quadrado 3x3
    let quadrados3x3 = []
    for (let socorro = 0;socorro < len(sudoku);socorro += 3) {
        for (let quadrado = 0;quadrado < len(sudoku);quadrado += 3) {
            let quadrado3x3 = []
            for (let i = socorro;i < socorro+3;i++) {
                for (let j = quadrado;j < quadrado+3;j++) {
                    quadrado3x3.push(sudoku[i][j])
                }
            }
            quadrados3x3.push("".join(quadrado3x3))
        }
    }

    for (let quadrado in quadrados3x3) {
        for (let num in quadrado) {
            numeros[num] += 1
        }

        for (let i = 1;i < 10;i++) {
            if (numeros[String(i)] !== 1) {
                return false
            }
            numeros[String(i)] = 0
        }
    }

    // verifica quadrado 3x3

    return true

}
