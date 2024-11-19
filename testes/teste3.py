#principal
core = True
menu = ""
melhorias = 0
algo = 0
quadrados = 0
click_base = 1
#fim do principal

#quadrados ascendentes
quadrados_ascendentes = -2
qua_as1 = 0
qua_as2 = 100000000
a_quadrados_as = 1 + (quadrados_ascendentes / 10)
renascimento = False
if qua_as1 > qua_as2:
    m_qua_as = qua_as1
if qua_as2 > qua_as1:
    m_qua_as = qua_as2
#fim dos quadrados ascendentes

#evento raro 1(clique critico)
import random
def evento_raro(chance_percentual):
    return random.random() < (chance_percentual / 100.0)
# Configurações
chance_de_evento = 3  # 1% de chance
numero_de_testes = 1
contador_de_eventos = 0
eventoraro = False
#fim do evento raro 1(clique critico)

#maquina da sorte
import random

def maquina_da_sorte(aposta):
    global quadrados
    
    if aposta > quadrados:
        print("Você não tem quadrados suficientes para fazer essa aposta!")
        return
    
    resultado = random.choice(['ganhar', 'perder'])
    
    if resultado == 'ganhar':
        quadrados += aposta  # Dobra os quadrados apostados
        print(f"Parabéns! Você ganhou {aposta} quadrados. Agora você tem {quadrados} quadrados.")
    else:
        quadrados -= aposta  # Perde os quadrados apostados
        print(f"Que pena! Você perdeu {aposta} quadrados. Agora você tem {quadrados} quadrados.")
#fim da maquina da sorte

#formatação dos numeros
def format_number(n):
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f}b"
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.2f}m"
    elif n >= 1_000:
        return f"{n / 1_000:.2f}k"
    else:
        return f"{n / 1:.2f}"


#fim da formatação dos nuemros

#contruçoes
cursores = 0
professores = 0
matematicos = 0
quadros = 0
fabricas = 0

v_cursores = 100 
v_professores = 5000
v_matematicos = 130000
v_quadros = 9000000
v_fabricas = 650000000

a_cursores = 1
a_professores = 10
a_matematicos = 50
a_quadros = 1000
a_fabricas = 1000

b1 = False
b2 = False
b3 = False
b4 = False
b5 = False

c1 = False
c2 = False
c3 = False
c4 = False
c5 = False

p1 = False
p2 = False
p3 = False
p4 = False
p5 = False

m1 = False
m2 = False
m3 = False
m4 = False
m5 = False

q1 = False
q2 = False
q3 = False
q4 = False
q5 = False

f1 = False
f2 = False
f3 = False
f4 = False
f5 = False
#fim das construçoes

#triangulos
triangulos = 0
tr1 = False
tr2 = False
tr3 = False
tr4 = False
tr5 = False
tr6 = False
tr7 = False
tr8 = False
tr9 = False
tr10 = False
#fim dos triangulos

#melhorias de triangulos
pd1 = False
cc1 = False
cm1 = False
sp1 = False
cq1 = False
ms1 = False
lm1 = False
qm1 = False
cz1 = False
a_pd1 = 1
#fim das melhorias de triangulos

#Salvamento
import json

def salvar_jogo(filename='savegame.json'):
    save_data = {

        #salvar o status das partes principais
        'core': core,
        'menu': menu,
        'quadrados': quadrados,
        'click_base': click_base,

        #salvar o status dos quadrados ascendentes
        'quadrados_ascendentes': quadrados_ascendentes,
        'qua_as1': qua_as1,
        'qua_as2': qua_as2,
        'm_qua_as': m_qua_as,

        #salvar o status do evento raro
        'chance_de_evento': chance_de_evento,
        'numero_de_testes': numero_de_testes,
        'contador_de_eventos': contador_de_eventos,
        'eventoraro': eventoraro,

        #salvar o status das construçoes
        'cursores': cursores,
        'professores': professores,
        'matematicos': matematicos,
        'quadros': quadros,
        'fabricas': fabricas,
        'v_cursores': v_cursores,
        'v_professores': v_professores,
        'v_matematicos': v_matematicos,
        'v_quadros': v_quadros,
        'v_fabricas': v_fabricas,
        'a_cursores': a_cursores,
        'a_professores': a_professores,
        'a_matematicos': a_matematicos,
        'a_quadros': a_quadros,
        'a_fabricas': a_fabricas,

        #salvar o status das melhorias
        'b1': b1,
        'b2': b2,
        'b3': b3,
        'b4': b4,
        'b5': b5,
        'c1': c1,
        'c2': c2,
        'c3': c3,
        'c4': c4,
        'c5': c5,
        'p1': p1,
        'p2': p2,
        'p3': p3,
        'p4': p4,
        'p5': p5,
        'm1': m1,
        'm2': m2,
        'm3': m3,
        'm4': m4,
        'm5': m5,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4,
        'q5': q5,
        'f1': f1,
        'f2': f2,
        'f3': f3,
        'f4': f4,
        'f5': f5,

        #salvar o status dos triângulos
        'tr1': tr1,
        'tr2': tr2,
        'tr3': tr3,
        'tr4': tr4,
        'tr5': tr5,
        'tr6': tr6,
        'tr7': tr7,
        'tr8': tr8,
        'tr9': tr9,
        'tr10': tr10,
        'triangulos': triangulos,

        #salvar o status das melhorias de triangulos
        'pd1': pd1, 
        'cc1': cc1, 
        'cm1': cm1,
        'sp1': sp1, 
        'cq1': cq1,
        'ms1': ms1, 
        'lm1': lm1, 
        'qm1': qm1, 
        'cz1': cz1, 
        'a_pd1': a_pd1,
    }
    with open(filename, 'w') as file:
        json.dump(save_data, file)
    print("Jogo salvo com sucesso.")

def carregar_jogo(filename='savegame.json'):
    global core, menu, quadrados, click_base, quadrados_ascendentes, qua_as1, qua_as2, m_qua_as
    global chance_de_evento, numero_de_testes, contador_de_eventos, eventoraro
    global cursores, professores, matematicos, quadros, fabricas
    global v_cursores, v_professores, v_matematicos, v_quadros, v_fabricas
    global a_cursores, a_professores, a_matematicos, a_quadros, a_fabricas 
    global melhorias, b1, b2, b3, b4, b5, c1, c2, c3, c4, c5, p1, p2, p3, p4, p5, m1, m2, m3, m4, m5, q1, q2, q3, q4, q5, f1, f2, f3, f4, f5
    global triangulos, tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10
    global pd1, cc1, cm1, sp1, cq1, ms1, lm1, qm1, cz1, a_pd1
    
    try:
        with open(filename, 'r') as file:
            save_data = json.load(file)

            #carregar o status das partes principais
            core = save_data['core']
            menu = save_data['menu']
            quadrados = save_data['quadrados']
            click_base = save_data['click_base']

            #carregar o status dos quadrados ascendentes
            quadrados_ascendentes = save_data['quadrados_ascendentes']
            qua_as1 = save_data['qua_as1']
            qua_as2 = save_data['qua_as2']
            m_qua_as = save_data['m_qua_as']

            #carregar o status do evento raro 
            chance_de_evento = save_data['chance_de_evento']
            numero_de_testes = save_data['numero_de_testes']
            contador_de_eventos = save_data['contador_de_eventos']
            eventoraro = save_data['eventoraro']

            #carregar o status das construçoes
            cursores = save_data['cursores']
            professores = save_data['professores']
            matematicos = save_data['matematicos']
            quadros = save_data['quadros']
            fabricas = save_data['fabricas']
            v_cursores = save_data['v_cursores']
            v_professores = save_data['v_professores']
            v_matematicos = save_data['v_matematicos']
            v_quadros = save_data['v_quadros']
            v_fabricas = save_data['v_fabricas']
            a_cursores = save_data['a_cursores']
            a_professores = save_data['a_professores']
            a_matematicos = save_data['a_matematicos']
            a_quadros = save_data['a_quadros']
            a_fabricas = save_data['a_fabricas']

            #carregar o status das melhorias
            b1 = save_data['b1']
            b2 = save_data['b2']
            b3 = save_data['b3']
            b4 = save_data['b4']
            b5 = save_data['b5']
            c1 = save_data['c1']
            c2 = save_data['c2']
            c3 = save_data['c3']
            c4 = save_data['c4']
            c5 = save_data['c5']
            p1 = save_data['p1']
            p2 = save_data['p2']
            p3 = save_data['p3']
            p4 = save_data['p4']
            p5 = save_data['p5']
            m1 = save_data['m1']
            m2 = save_data['m2']
            m3 = save_data['m3']
            m4 = save_data['m4']
            m5 = save_data['m5']
            q1 = save_data['q1']
            q2 = save_data['q2']
            q3 = save_data['q3']
            q4 = save_data['q4']
            q5 = save_data['q5']
            f1 = save_data['f1']
            f2 = save_data['f2']
            f3 = save_data['f3']
            f4 = save_data['f4']
            f5 = save_data['f5']

            #Carregar o status dos triângulos
            tr1 = save_data['tr1']
            tr2 = save_data['tr2']
            tr3 = save_data['tr3']
            tr4 = save_data['tr4']
            tr5 = save_data['tr5']
            tr6 = save_data['tr6']
            tr7 = save_data['tr7']
            tr8 = save_data['tr8']
            tr9 = save_data['tr9']
            tr10 = save_data['tr10']
            triangulos = save_data['triangulos']

            #carregar o status das melhorias de triangulos
            pd1 = save_data['pd1']
            cc1 = save_data['cc1']
            cm1 = save_data['cm1']
            sp1 = save_data['sp1']
            cq1 = save_data['cq1']
            ms1 = save_data['ms1']
            lm1 = save_data['lm1']
            qm1 = save_data['qm1']
            cz1 = save_data['cz1']
            a_pd1 = save_data["a_pd1"]

        print("Jogo carregado com sucesso.")
    except FileNotFoundError:
        print("Arquivo de salvamento não encontrado.")
#fim do salvamento


while core == True:

    if renascimento == False:
        quadrado_click = ((click_base + (a_cursores * cursores) + (a_professores * professores) + (a_matematicos * matematicos) + (a_quadros * quadros) + (a_fabricas * fabricas)) * a_pd1)
    if renascimento == True:
        quadrado_click = ((click_base + (a_cursores * cursores) + (a_professores * professores) + (a_matematicos * matematicos) + (a_quadros * quadros) + (a_fabricas * fabricas)) * a_quadrados_as * a_pd1)

    if quadrados == qua_as1:
        qua_as1 = qua_as1 + qua_as2
        quadrados_ascendentes += 1
    if quadrados == qua_as2:
        qua_as2 = qua_as1 + qua_as2
        quadrados_ascendentes += 1

    if menu == "":
        print('''\n\n
          QUADRADO CLICKER                              
                                                          
     Quadrados por click:''',format_number(quadrado_click),'''                                 
            ____________            Quadrados:''',format_number(quadrados),'''                   
Aperte     |            |           Triângulos:''',int(triangulos),'''                   
"Enter"    |            |           _________________________________    _________________________________
para gerar |            |          |                                 |  |                                 |
quadrados  |            |          |   Digite "melhorias" para       |  |   Digite "ajuda" para acessar   |
           |____________|          |   acessar o menu de melhorias   |  |         o menu de ajuda         |
                                   |_________________________________|  |_________________________________|

      Digite o numero da construção para compra-la
 ____________________________________________________________________________________________________________ 
|    __         _    __    ___    _    __   __                          Possui:''',cursores,''' 
|   /    |  |  |_)  (__   /   \  |_)  |__  (__                          Preço:''',format_number(v_cursores),'''
|   \__  |__|  |\    __)  \___/  |\   |__   __)                         Aumento:''',a_cursores,'''
|____________________________________________________________________________________________________________
|    __    _    ___    __   __   __   __    ___    _    __   __         Possui:''',professores,'''
|   |__)  |_)  /   \  |__  |__  (__  (__   /   \  |_)  |__  (__         Preço:''',format_number(v_professores),'''
|   |     |\   \___/  |    |__   __)  __)  \___/  |\   |__   __)        Aumento:''',a_professores,'''
|____________________________________________________________________________________________________________
|             _   ___   __            _   ___      __   ___    __       Possui:''',matematicos,'''            
|   |\  /|   /_\   |   |__  |\  /|   /_\   |   |  /    /   \  (__       Preço:''',format_number(v_matematicos),'''
|   | \/ |  /   \  |   |__  | \/ |  /   \  |   |  \__  \___/   __)      Aumento:''',a_matematicos,'''
|____________________________________________________________________________________________________________
|    __            _     __    _    ___    __                           Possui:''',quadros,'''         
|   | _|   |  |   /_\   |  \  |_)  /   \  (__                           Preço:''',format_number(v_quadros),'''
|   |__|\  |__|  /   \  |__/  |\   \___/   __)                          Aumento:''',a_quadros,'''        
|____________________________________________________________________________________________________________
|    __    _     __    _       __    _     __                           Possui:''', fabricas,'''
|   |__   /_\   |__)  |_)  |  /     /_\   (__                           Preço:''',format_number(v_fabricas),'''  
|   |    /   \  |__)  |\   |  \__  /   \   __)                          Aumento:''',a_fabricas,'''
|____________________________________________________________________________________________________________


''')
    
    elif menu == "melhorias" and cq1 == False:
        print('''\n\n\n\n\n\n\n\n
                                         __              ___    _        _     __
                                |\  /|  |__  |    |__|  /   \  |_)  |   /_\   (__
                                | \/ |  |__  |__  |  |  \___/  |\   |  /   \   __)

    Digite a letra e o numero ao lado da melhoria para compra-la
    Aperte "Enter" para voltar ao menu principal
 _______________________________________________________________________ ___________________________________ ___________________________________ ___________________________________ ___________________________________
|          Clique duplo-b1          |          Super clique-b2          |        Mega clique  clique        |           Ultra clique            |          Clique supremo           |            Em breve               |
| O clique base é 2x mais eficiente |O clique base é 300x mais eficiente|O clique base é 100x mais eficiente|                                   |                                   |                                   |
|                                   |                                   |                                   |                                   |                                   |                                   |
|Preço:70                           |preço:300k                         |preço:20m                          |                                   |                                   |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|
|        Cursores duplos-c1         |        Multiplos cursores-c2      |            Super cursores         |         Mega cursores             |       Cursores gigantescos        |                                   |
|  Cursores são 2x mais eficientes  | cursores são 5x mais eficientes   | Cursores são 20x mais eficientes  |                                   |                                   |                                   |
|                                   |                                   |                                   |                                   |                                   |                                   |
|Preço:750                          |preço:75k                          |preço:10m                          |                                   |                                   |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|
|       Professores duplos-p1       |            Escola-p2              |          Super professores        |     Sindicato dos professores     |        Ensino superfaturado       |
|professores são 2x mais eficientes |professores são 5x mais eficientes |professores são 20x mais eficientes|
|                                   |                                   |
|Preço:25k                          |preço:600k                         |preço:90m   
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|
|        Matematica dupla-m1        |     Conjuto de matematicos-m2     |          Super matematicos        |         Mega matematicos          |       Ordem dos intelectuais      |
|matematicos são 2x mais eficientes |matematicos são 5x mais eficientes |
|                                   |                                   |
|preço:600k                         |preço:20m                          |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________
|          Dois quadros-q1          |            Quadrão-q2             |           Quadros poderosos       |            Pinacoteca             |           Telas digitais          |
|  quadros são 2x mais eficientes   |  quadros são 5x mais eficientes   |
|                                   |                                   |
|preço:30m                          |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________
|         Duas fabricas-f1          |      Começo da revolução-f2       |             Super fabricas        |           Mega fabricas           |      5° Revolução industrial      |
|  fabricas são 2x mais eficientes  |  fabricas são 5x mais eficientes  |         
|                                   |                                   |
|                                   |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________

''')

    elif menu == "melhorias" and cq1 == True:
        print('''\n\n\n\n\n\n\n\n
                                         __              ___    _        _     __
                                |\  /|  |__  |    |__|  /   \  |_)  |   /_\   (__
                                | \/ |  |__  |__  |  |  \___/  |\   |  /   \   __)

    Digite a letra e o numero ao lado da melhoria para compra-la
    Aperte "Enter" para voltar ao menu principal
 _______________________________________________________________________ ___________________________________ ___________________________________ ___________________________________ ___________________________________
|          Clique duplo-b1          |          Super clique-b2          |        Mega clique  clique        |           Ultra clique            |          Clique supremo           |             Em breve              |
| O clique base é 2x mais eficiente |O clique base é 300x mais eficiente|O clique base é 100x mais eficiente|                                   |                                   |                                   |
|                                   |                                   |                                   |                                   |                                   |                                   |
|Preço:70                           |preço:300000                       |preço:20000000                     |                                   |                                   |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|
|        Cursores duplos-c1         |        Multiplos cursores-c2      |            Super cursores         |         Mega cursores             |       Cursores gigantescos        |                                   |
|  Cursores são 2x mais eficientes  | cursores são 5x mais eficientes   | Cursores são 20x mais eficientes  |                                   |                                   |                                   |
|                                   |                                   |                                   |                                   |                                   |                                   |
|Preço:750                          |preço:75000                        |preço:10000000                     |                                   |                                   |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|
|       Professores duplos-p1       |            Escola-p2              |          Super professores        |     Sindicato dos professores     |        Ensino superfaturado       |
|professores são 2x mais eficientes |professores são 5x mais eficientes |professores são 20x mais eficientes|
|                                   |                                   |
|Preço:25000                        |preço:600000                       |preço:90000000
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|
|        Matematica dupla-m1        |     Conjuto de matematicos-m2     |          Super matematicos        |         Mega matematicos          |       Ordem dos intelectuais      |
|matematicos são 2x mais eficientes |matematicos são 5x mais eficientes |
|                                   |                                   |
|preço:600000                       |preço:20000000                     |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________
|          Dois quadros-q1          |            Quadrão-q2             |           Quadros poderosos       |            Pinacoteca             |           Telas digitais          |
|  quadros são 2x mais eficientes   |  quadros são 5x mais eficientes   |
|                                   |                                   |
|preço:30000000                     |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________
|         Duas fabricas-f1          |      Começo da revolução-f2       |             Super fabricas        |           Mega fabricas           |      5° Revolução industrial      |
|  fabricas são 2x mais eficientes  |  fabricas são 5x mais eficientes  |         
|                                   |                                   |
|                                   |                                   |
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________
|      
|
|      
|
|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________|___________________________________

              
''')

    elif menu == "ajuda":
        print('''\n\n\n\n\n\n\n\n\n\n\n\n\n
Basico:
              
-Para ganhar "quadrados" aperte a tecla "enter"
              
-A quantidade de "quadrados" ganhos por clique é indicada pelo numero ao lado de "Quadrados por click",
localizado acima do grande quadrado
              
-Existem, atualmente, 5 contruçoes diferentes: "cursores","professores","matematicos","quadros", e 
"fabricas", para compra-las basta ter o numero de quadrados indicado pelo "preço" e digitar o numero
da contrução desejada,1 para cursores, 2 para professores, 3 para matematicos e assim por diante

                          
Melhorias:
              
-Existem 6 tipos de melhorias: 1 para cada contrução e 1 para o clique base(começa como 1)
              
-Cada tipo de melhoria possui 5 melhorias, quanto mais alto o nivel da melhoria, mais caro

-Para comprar a melhoria, digite a letra inicial da contrução e o numero da melhoria, que está indicada 
ao lado do nome da melhoria(Para a melhoria de clique base, a letra é b)
              
-OBS:Você não precisa estar no menu melhorias para poder comprar uma melhoria
              

Triângulos:
              
-Triângulos são uma moeda rara que podem ser usadas para obterr melhorias especiais
              
-Para obter triângulos, você precisa conseguir uma determinada quantidade de quadrados
              
-O numero de quadrados necessarios para conseguir um triângulo começa com 1000, depois 100000, depois 
multiplicando por 100 para cada triângulo
              
-Esse numero reseta para 1000 ao renascer
              
-Para poder comprar as melhorias com triângulos, digite "triangulos" e aperte "enter", isso te levará
a um menu onde você poderá ver as melhorias disponiveis
              
-Para comprar as melhorias basta digitar a/as letras e o numero ao lado do nome da melhorias, de forma
similar as melhorias normais
              
-Toda a loja desse menu está com o preço em triângulos
                            

Renascimentos: 

-Renascer fará com que você perca todos os seus quadrados, melhorias e construções

-Para renascer digite "renascer" e depois aperte "enter", depois digite "confirmar" e aperte "enter"

-Renascer te dará um bônus de 10% de forma somativa para cada "quadrado ascendente" que você tiver
              
-Você obtém quadrados ascendentes ao conseguir determinado numero de quadrados normais
              
-Você pode renascer quando tiver conseguido no minimo 1 quadrado ascendente
              
-Você começa a produzir quadrados ascendentes a partir de 100000000 de quadrados normais
              

Salvamento:
              
-Para salvar o jogo digite "salvamento", isso te levará a um menu diferente, neste menu digite "salvar"
              
-Salvar o jogo criará um arquivo com o nome savegame.json, esse arquivo contem todas as informações do 
seu save
              
-Esse arquivo deve ficar no mesmo local em que o jogo está armazenado
              
-Para carregar um jogo salvo, digite "carregar" no menu de salvamento, isso só funcionará se você
tiver o arquivo salvo
              
-OBS:Se você ja tiver um arquivo de salvamento, e salvar o jogo, o primeiro arquivo será perdido e será
substituido pelo atual, para evitar isso, tranfira o arquivo para outro local e depois salve o jogo, 
dessa forma você terá 2 arquivos 
              

Minijogos:
              
-Existem 4 minijogos, cada um adiciona algo diferente ao jogo base, para desbloquea-los, é necessario 
compra-los com triângulos
              
-Maquina da sorte:
              
-Livro magico:
              
-Quiz matemático:
              
-Cozinha:Usa ingredientes que custam quadrados, cada ingrediente faz algo, maximo de (nao sei ainda) por nascimento, uma receita tem (nao sei ainda) ingredientes


''')
    
    elif menu == "renascer":
        print('''\n\n
              
                            _    __          _     __    __   __   _
                           |_)  |__  |\ |   /_\   (__   /    |__  |_)
                           |\   |__  | \|  /   \   __)  \__  |__  |\ 
              


-Ao renascer, você perderá todos os seus quadrados, contruções e melhorias, mas manterá seus triângulos
e quadrados ascendentes

-Você começa a produzir quadrados ascendentes quando ultrapassa 100000000 de quadrados
              
-Você possui''',quadrados_ascendentes,'''quadrados ascendentes

-Você pode renascer quando tiver pelo menos 1 quadrado ascendente
              

Você tem certeza que deseja continuar?
             

Digite confirmar para continuar





\n\n\n\n\n\n
''')

    elif menu == "renascimento":
        print('''





''')

    elif menu == "triangulos":
        print('''

                ___   _        _           __               ___    __
                 |   |_)  |   /_\   |\ |  | _   |  |  |    /   \  (__
                 |   |\   |  /   \  | \|  |__|  |__|  |__  \___/   __)

OBS:Todos os preços nesta seção estão em triângulos

Produtividade dobrada-pd1:
Dobra seus quadrados por clique
Preço:2 
              
Clique crítico-cc1:
Há uma pequena chance de conseguir um clique crítico, que dá 5x quadrados
Preço:1
              
Crítico melhorado-cm1:
(Necessita do clique crítico desbloqueado)
O crítico tem 2x mais chance de ocorrer e gera 15x mais quadrados em vez de 5x
Preço:1

Superprodução-sp1:
Todas as construçôes são 100% mais eficientes
Preço:2

Caixa de quadrados-cq1:
Adiciona melhorias normais
Preço:2

Maquina da sorte-ms1:
Adiciona um minijogo em que você pode apostar seus quadrados
Preço:3
              
Livro magico-lm1:
Adiciona um mini jogo em que você pode usar feitiços que ajudam no jogo principal
Preço:3
              
Quiz matemático-qm1:
Adiciona um mini jogo em que você responde um quiz, se acertar ganha recompensas
Preço:3

Cozinha-cz1:
Adiciona um mini jogo em que você pode preparar comidas que podem te ajudar
Preço:3             


''')

    elif menu == "salvamento":
        print('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

-Para salvar o jogo digite "salvar"
              
-Para carregar um jogo digite "carregar"

-Para mais informações veja o menu de ajuda

\n\n\n\n\n\n\n\n\n\n\n
''')

    elif menu == "maquina da sorte":
        print('''

 ______________________________
|                              |
|       Maquina da sorte       |
|______________________________|   ___                    Aposte uma quantidade de quadrados,
|                              |  /   \                   se você ganhar a aposta, os quadrados
|------------------------------|  \___/                   apostados são dobrados, caso constrario,
|                              |   //                     você perde tudo
|   $     $     $     $     $  |  //
|                              | //                       Para realizar a aposta, digite "apostar"
|------------------------------|//   
|                              |/                         Se você quiser cancelar a aposta, digite "0"
|   7     7     7     7     7  |
|                              |
|------------------------------|
|                              |
|   $     $     $     $     $  |
|                              |
|------------------------------|


''')

    algo = input()

    if algo == "":
        quadrados += quadrado_click
        menu = ""

        # Executando os testes
        for _ in range(numero_de_testes):
            if evento_raro(chance_de_evento):
                contador_de_eventos += 1
                eventoraro = True
   
    if algo == "1" and quadrados >= v_cursores:
        cursores += 1
        quadrados = quadrados - v_cursores
        v_cursores = v_cursores * 1.1

    if algo == "2" and quadrados >= v_professores:
        professores += 1
        quadrados = quadrados - v_professores
        v_professores = v_professores * 1.1

    if algo == "3" and quadrados >= v_matematicos:
        matematicos += 1
        quadrados = quadrados - v_matematicos
        v_matematicos = v_matematicos * 1.1

    if algo == "4" and quadrados >= v_quadros:
        quadros += 1
        quadrados = quadrados - v_quadros
        v_quadros = v_quadros * 1.1

    if algo == "5" and quadrados >= v_fabricas:
        fabricas += 1
        quadrados = quadrados - v_fabricas
        v_fabricas = v_fabricas * 1.1

    #melhorias
    if algo == "b1" and b1 == False and quadrados >= 70:
        click_base = click_base * 2
        b1 = True
        quadrados = quadrados - 70

    if algo == "b2" and b2 == False and quadrados >= 300000:
        click_base = click_base * 300
        b2 = True
        quadrados = quadrados - 300000

    if algo == "b3" and b3 == False and quadrados >= 20000000:
        click_base = click_base * 100
        b3 = True
        quadrados = quadrados - 20000000

    if algo == "b4" and b4 == False and quadrados >= 0:
        print()

    if algo == "b5" and b5 == False and quadrados >= 0:
        print()

    if algo == "c1" and c1 == False and quadrados >=750:
        a_cursores = a_cursores * 2 
        c1 = True   
        quadrados = quadrados - 750 

    if algo == "c2" and c2 == False and quadrados >= 75000:
        a_cursores = a_cursores * 5
        c2 = True
        quadrados = quadrados - 75000

    if algo == "c3" and c3 == False and quadrados >= 10000000:
        a_cursores = a_cursores * 20
        c3 = True
        quadrados = quadrados - 10000000

    if algo == "c4" and c4 == False and quadrados >= 0:
        print()

    if algo == "c5" and c5 == False and quadrados >= 0:
        print()

    if algo == "p1" and p1 == False and quadrados >= 25000:  
        a_professores = a_professores * 2
        p1 = True
        quadrados = quadrados - 25000

    if algo == "p2" and p2 == False and quadrados >= 600000: 
        a_professores = a_professores * 5
        p2 = True
        quadrados = quadrados - 600000

    if algo == "p3" and p3 == False and quadrados >= 90000000: 
        a_professores = a_professores * 20
        p3 = True
        quadrados = quadrados - 90000000

    if algo == "p4" and p4 == False and quadrados >= 0: 
        print()

    if algo == "p5" and p5 == False and quadrados >= 0: 
        print()

    if algo == "m1" and m1 == False and quadrados >= 600000:
        a_matematicos = a_matematicos * 2
        m1 = True
        quadrados = quadrados - 600000

    if algo == "m2" and m2 == False and quadrados >= 20000000:
        a_matematicos = a_matematicos * 5
        m2 = True
        quadrados = quadrados - 20000000

    if algo == "m3" and m3 == False and quadrados >= 0:
        print()

    if algo == "m4" and m4 == False and quadrados >= 0:
        print()

    if algo == "m5" and m5 == False and quadrados >= 0:
        print()

    if algo == "q1" and q1 == False and quadrados >= 30000000:
        a_quadros = a_quadros * 2
        q1 = True
        quadrados = quadrados - 30000000
    
    if algo == "q2" and q2 == False and quadrados >= 0:
        print()

    if algo == "q3" and q3 == False and quadrados >= 0:
        print()

    if algo == "q4" and q4 == False and quadrados >= 0:
        print()

    if algo == "q5" and q5 == False and quadrados >= 0:
        print()

    if algo == "f1" and f1 == False and quadrados >= 0:
        print()

    if algo == "f2" and f2 == False and quadrados >= 0:
        print()

    if algo == "f3" and f3 == False and quadrados >= 0:
        print()

    if algo == "f4" and f4 == False and quadrados >= 0:
        print()

    if algo == "f5" and f5 == False and quadrados >= 0:
        print()
    #fim das melhorias

    #menus
    if algo == "melhorias":
        menu = "melhorias"

    if algo == "ajuda":
        menu = "ajuda"

    if algo == "renascer":
        menu = "renascer"

    if algo == "salvamento":
        menu = "salvamento"

    if algo == "triangulos":
        menu = "triangulos"

    if algo == "ms":
        menu = "maquina da sorte"

    #fim dos menus

    #cheats
    if algo == "give1000":
        quadrados = quadrados + 1000

    if algo == "give100k":
        quadrados = quadrados + 100000

    if algo == "give10m":
        quadrados = quadrados + 10000000

    if algo == "give1b":
        quadrados = quadrados + 1000000000
    #fim dos cheats

    #triângulos
    if quadrados >= 1000 and tr1 == False:
        triangulos += 1
        tr1 = True
    
    if quadrados >= 100000 and tr2 == False:
        triangulos += 1
        tr2 = True

    if quadrados >= 10000000 and tr3 == False:
        triangulos += 1
        tr3 = True

    if quadrados >= 1000000000 and tr4 == False:
        triangulos += 1
        tr4 = True

    if quadrados >= 100000000000 and tr5 == False:
        triangulos += 1
        tr5 = True
    #fim dos triângulos
    
    #renascimento
    if algo == "confirmar" and menu == "renascer" and quadrados_ascendentes >= 1:
        quadrados = 0
        click_base = 1
        menu = ""
        renascimento = True

        b1 = False
        b2 = False
        b3 = False
        b4 = False
        b5 = False

        c1 = False
        c2 = False
        c3 = False
        c4 = False
        c5 = False

        p1 = False
        p2 = False
        p3 = False
        p4 = False
        p5 = False

        m1 = False
        m2 = False
        m3 = False
        m4 = False
        m5 = False

        q1 = False
        q2 = False
        q3 = False
        q4 = False
        q5 = False

        f1 = False
        f2 = False
        f3 = False
        f4 = False
        f5 = False
        
        cursores = 0
        professores = 0
        matematicos = 0
        quadros = 0
        fabricas = 0

        v_cursores = 100
        v_professores = 5000
        v_matematicos = 130000
        v_quadros = 9000000
        v_fabricas = 650000000

        a_cursores = 1
        a_professores = 10
        a_matematicos = 50
        a_quadros = 1000
        a_fabricas = 1000

        tr1 = False
        tr2 = False
        tr3 = False
        tr4 = False
        tr5 = False
        tr6 = False
        tr7 = False
        tr8 = False
        tr9 = False
        tr10 = False
    #fim do renascimento

    #salvamento
    if algo == "salvar" and menu == "salvamento":
        salvar_jogo()

    if algo == "carregar" and menu == "salvamento":
        carregar_jogo()
    #fim do salvamento

    #melhorias dos triangulos
    if algo == "pd1" and menu == "triangulos" and triangulos >= 2:
        pd1 = True
        a_pd1 = 2
        triangulos = triangulos - 2

    if algo == "cc1" and menu == "triangulos" and triangulos >= 1:
        cc1 = True
        triangulos = triangulos - 1

    if algo == "cm1" and menu == "triangulos" and cc1 == True and triangulos >= 1:
        cm1 = True
        chance_de_evento = chance_de_evento * 2
        triangulos = triangulos - 1

    if algo == "sp1" and menu == "triangulos" and triangulos >= 2:
        sp1 = True
        a_cursores = a_cursores * 2
        a_professores = a_professores * 2
        a_matematicos = a_matematicos * 2
        a_quadros = a_quadros * 2
        a_fabricas = a_fabricas * 2
        triangulos = triangulos - 2

    if algo == "cq1" and menu == "triangulos" and triangulos >= 2:
        cq1 = True
        triangulos = triangulos - 2

    if algo == "ms1" and menu =="triangulos" and triangulos >= 3:
        ms1 = True
        triangulos = triangulos - 2

    #fim das melhorias dos triangulos

    #clique critico
    if eventoraro == True and cc1 == True and cm1 == False:
        quadrados = quadrados + (4 * quadrado_click)
        eventoraro = False

    if eventoraro == True and cc1 == True and cm1 == True:
        quadrados = quadrados + (14 * quadrado_click)
        eventoraro = False
    #fim do clique critico

    #maquina da sorte 
    if algo == "apostar" and menu == "maquina da sorte":
        while True:
            try:
                aposta = int(input("Digite quanto você deseja apostar:"))
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite um número válido.")
        
        maquina_da_sorte(aposta)

    #fim da maquina da sorte