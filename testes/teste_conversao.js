function len(x) {
    return x.length()
}
let lista = ["ola", 1, true, false, 32.32]

function ola(x) {

    if ((true)) {

        let contador = 1

        while (x <= 3) {  

            if (x < 1) {

                console.log("ola", contador)

                console.log("ola", contador)
            }

            else if (x === 1) {
                console.log("Só ola")
            }

            else {
                console.log("Cavalo")
            }

            contador += 1
            x += 1
        }
    }

    let ola = "hmmmm"
    console.log(len(ola))

    for (let i = -3;i < 7;i += 2) {
        console.log("Batata"+i)
    }

    for (let item in lista) {
        console.log(item)
    }
}

function algo() {
    //dsfddsfsdfdsfd
    console.log("algo")
}

class Jurandy {

    static var_legal = 13

    constructor( estado_computador="Usando",objeto_bolsa="Bolas") {
    }

    turtle() {
        console.log(`Para não se confundir, import turtle como tartaruga`)
    }

    padrão() {
        console.log(`O seu código tem um padrão?Digite sim ou não:`)
        let tem_padrao = window.prompt()

        if (tem_padrao === "sim") {
            console.log(`Muito bem! seu código tem padrão`)
        }
        if (tem_padrao === "não") {
            console.log(`Seu código não tem padrão! Isso é inaceitável, seu código não vale de nada`)
        }
    }

    filho() {
        console.log(`O meu filho Hugo, ele gosta muito de aviões, numberblocks, e inglês`)
    }

    aula() {
        console.log(`Sim é claro, sobre a aula, vamos aprender sobre funções, então vou começar fazendo uma relação com meu filho`)
        this.filho()
    }

    numberblocks() {
        console.log(`Aventure-se em um mundo de diversão com os números no programa de sucesso do canal CBeebies, os Numberblocks. Personagens vencedores de prêmios + grandes aventuras + músicas = a melhor maneira de empolgar as crianças com todo o potencial dos números! A matemática torna-se MUITO mais fácil quando você consegue ver como ela funciona. 90 episódios dão vida a inúmeras habilidades essenciais com os números por meio de um formidável visual e uma animação fabulosa, desde o seu primeiro encontro com a Um até minimusicais, comédia clássica, apresentações de música e dança e uma inquietante fuga do Calabouço Duplo...`)
    }

    oulu() {
        console.log(`Na aula de hoje, vamos usar o oulu, já que ele é 100% necessário, para isso vocês devem digitar o seguinte comando no cmd, vou escrever no quadro o comando, e não se preocupem sobre entender cada coisa, depois eu explico`)
    }

    IDLE() {
        console.log(`Para que vocês não se confundam, eu fortemente recomendo usar o IDLE em vez do VsCode, já que ele é muito mais simples`)
    }

    PC() {
        if (this.computador === "Usando") {
            console.log(`Para não ficarem distraídos, NÃO abram o Google`)
        }
        else if (this.computador === "Desligado") {
            console.log(`Não liguem o computador ainda, olhem para o quadro`)
        }
        else {
            console.log("Prestem atenção nesse papel que eu vou dar para vocês")
        }
    }

    eh_para_copiar() {
        console.log(`Eu vou cobrar isso, então é bom você copiarem, pois só entra na proxima aula quem tiver copiado`)
    }

    domingo_noite() {
        console.log(`Vocês sabem o que eu faço domingo a noite? Isso mesmo! Eu faço programa`)
    }

    bolsa() {
        if (this.objeto_bolsa === "Bolas") {
            console.log(`Hoje eu trouxe 12 bolas para mostrar sobre padrão`)
        }
        else if (this.objeto_bolsa === "Maquina de datilografia") {
            console.log(`A chamada hoje será por meio de uma maquina de datilografia, agora vou explicar a história dela`)
        }
        else if (this.objeto_bolsa === "Cebola") {
            console.log(`Eu trouxe essa cebolas para podermos analisarmos o padrão nelas`)
        }
        else {
            this.numberblocks()
        }
    }

    duvida() {
        console.log(`Se você está com duvida no conteúdo, você deve pedir ajuda ao ChatGPT ou outra inteligências artificias`)
    }

    aprender() {
        console.log(`A escola não é para aprender, é para entender`)
    }

    help() {
        console.log(`Esse método é para ajudar quem precisar com essa classe, se você quiser ver todos os métodos, digite: prNumber(dir(Jurandy)), e todos os método apareceram(ignore os que começão com __). Outra informação, está classe usa 2 argumentos, o primeiro é estado_computador(defina como Usando ou Desligado para mensagens especiais, qualquer outra coisa resultará na mesma mensagem), o segundo é objeto_bolsa(defina como Bolas, Cebola ou Maquina de datilografia para mensagens especiais)`)
    }
}

try {
    let x = 1/0
}

catch(error) {

    console.log(`${lista}`)
}

teste_lambdas = (x,y) => {return x+y}
//(x,y) > return x+y
batata = (x) => {return x**3}

for (let x,y = 0;x,y < 10;x,y++) {
    console.log(x)
    for (let i = 0;i < y;i++) {
        console.log(i)
    }
}

let sudoku = [1,2,3,4,5,6,7,8,9]

for (const [index, linha] of sudoku.entries()) {
    sudoku[index] = String(linha)
}

//for (const [index,linha] of sudoku.entries()) {

