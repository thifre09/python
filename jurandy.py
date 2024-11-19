class Jurandy():

    def __init__(self, estado_computador="Usando",objeto_bolsa="Bolas"):
        self.computador = estado_computador
        self.objeto_bolsa = objeto_bolsa
    
    def turtle(self):
        print(f"Para não se confundir, import turtle como tartaruga")
    
    def padrão(self):
        print(f"O seu código tem um padrão?Digite sim ou não:")
        tem_padrao = input()

        if tem_padrao == "sim":
            print(f"Muito bem! seu codigo tem padrão")
        if tem_padrao == "não":
            print(f"Seu código não tem padrão! Isso é inaceitavel, seu código não vale de nada")

    def filho(self):
        print(f"O meu filho Hugo, ele gosta muito de aviões, numberblocks, e inglês")

    def aula(self):
        print(f"Sim é claro, sobre a aula, vamos aprender sobre funções, então vou começar fazendo uma relação com meu filho")
        self.filho()
    
    def numberblocks(self):
        print(f"Aventure-se em um mundo de diversão com os números no programa de sucesso do canal CBeebies, os Numberblocks. Personagens vencedores de prêmios + grandes aventuras + músicas = a melhor maneira de empolgar as crianças com todo o potencial dos números! A matemática torna-se MUITO mais fácil quando você consegue ver como ela funciona. 90 episódios dão vida a inúmeras habilidades essenciais com os números por meio de um formidável visual e uma animação fabulosa, desde o seu primeiro encontro com a Um até minimusicais, comédia clássica, apresentações de música e dança e uma inquietante fuga do Calabouço Duplo...")

    def oulu(self):
        print(f"Na aula de hoje, vamos usar o oulu, já que ele é 100% necessário, para isso vocês devem digitar o seguinte comando no cmd, vou escrever no quadro o comando, e não se preocupem sobre entender cada coisa, depois eu explico")
    
    def IDLE(self):
        print(f"Para que vocês não se confundam, eu fortemente recomendo usar o IDLE em vez do VsCode, já que ele é muito mais simples")

    def PC(self):
        if self.computador == "Usando":
            print(f"Para não ficarem distraidos, NÃO abram o Google")
        elif self.computador == "Desligado":
            print(f"Não liguem o computador ainda, olhem para o quadro")
        else:
            print("Prestem atenção nesse papel que eu vou dar para vocês")

    def eh_para_copiar(self):
        print(f"Eu vou cobrar isso, então é bom você compiarem, pois só entra na proxima aula quem tiver copiado")

    def domingo_noite(self):
        print(f"Vocês sabem o que eu faço domingo a noite? Isso mesmo! Eu faço programa")

    def bolsa(self):
        if self.objeto_bolsa == "Bolas":
            print(f"Hoje eu trouxe 12 bolas para mostrar sobre padrão")
        elif self.objeto_bolsa == "Maquina de datilografia":
            print(f"A chamada hoje será por meio de uma maquina de datilogradia, agora vou explicar a história dela")
        elif self.objeto_bolsa == "Cebola":
            print(f"Eu trouxe essa cebolas para podermos analizarmos o padrão nelas")
        else:
            self.numberblocks()

    def duvida(self):
        print(f"Se você está com duvida no conteudo, você deve pedir ajuda ao ChatGPT ou outra inteligências artificias")

    def aprender(self):
        print(f"A escola não é para aprender, é para entender")

    def help(self):
        print(f"Esse método é para ajudar quem precisar com essa classe, se você quiser ver todos os métodos, digite: print(dir(Jurandy)), e todos os metodo apareceram(ignore os que começão com '__'). Outra informação, está classe usa 2 argumentos, o primeiro é estado_computador(defina como 'Usando' ou 'Desligado' para menssagens especiais, qualquer outra coisa resultará na mesma menssagem), o segundo é objeto_bolsa(defina como 'Bolas', 'Cebola' ou 'Maquina de datilografia' para menssagens especiais)")



jurandy = Jurandy()
jurandy.numberblocks()