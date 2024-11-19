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
if qua_as1 > qua_as2:
    m_qua_as = qua_as1
if qua_as2 > qua_as1:
    m_qua_as = qua_as2
#fim dos quadrados ascendentes

#evento raro 1
import random
def evento_raro(chance_percentual):
    return random.random() < (chance_percentual / 100.0)
# Configurações
chance_de_evento = 1  # 1% de chance
numero_de_testes = 1
contador_de_eventos = 0
eventoraro = False
#fim do evento raro 1

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

import json

def salvar_jogo(filename='savegame.json'):
    save_data = {
        'core': core,
        'menu': menu,
        'quadrados': quadrados,
        'click_base': click_base,
        'quadrados_ascendentes': quadrados_ascendentes,
        'qua_as1': qua_as1,
        'qua_as2': qua_as2,
        'm_qua_as': m_qua_as,
        'chance_de_evento': chance_de_evento,
        'numero_de_testes': numero_de_testes,
        'contador_de_eventos': contador_de_eventos,
        'eventoraro': eventoraro,
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
        'melhorias': melhorias,
        'triangulos': triangulos,
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
    global melhorias, triangulos
    
    try:
        with open(filename, 'r') as file:
            save_data = json.load(file)
            core = save_data['core']
            menu = save_data['menu']
            quadrados = save_data['quadrados']
            click_base = save_data['click_base']
            quadrados_ascendentes = save_data['quadrados_ascendentes']
            qua_as1 = save_data['qua_as1']
            qua_as2 = save_data['qua_as2']
            m_qua_as = save_data['m_qua_as']
            chance_de_evento = save_data['chance_de_evento']
            numero_de_testes = save_data['numero_de_testes']
            contador_de_eventos = save_data['contador_de_eventos']
            eventoraro = save_data['eventoraro']
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
            melhorias = save_data['melhorias']
            triangulos = save_data['triangulos']
        print("Jogo carregado com sucesso.")
    except FileNotFoundError:
        print("Arquivo de salvamento não encontrado.")



while core == True:

    quadrado_click = click_base + (a_cursores * cursores) + (a_professores * professores) + (a_matematicos * matematicos) + (a_quadros * quadros) + (a_fabricas * fabricas)

    if quadrados == qua_as1:
        qua_as1 = qua_as1 + qua_as2
        quadrados_ascendentes += 1
    if quadrados == qua_as2:
        qua_as2 = qua_as1 + qua_as2
        quadrados_ascendentes += 1


    if menu == "":
        print('''\n\n
          QUADRADO CLICKER                              
                                                          
     Quadrados por click:''',quadrado_click,'''        Quadrados:''',int(quadrados),'''                          
            ____________            Triângulos:''',int(triangulos),'''                   
Aperte     |            |                             
"Enter"    |            |           _________________________________    _________________________________
para gerar |            |          |                                 |  |                                 |
quadrados  |            |          |   Digite "melhorias" para       |  |   Digite "ajuda" para acessar   |
           |____________|          |   acessar o menu de melhorias   |  |         o menu de ajuda         |
                                   |_________________________________|  |_________________________________|

      Digite o numero da construção para compra-la
 ____________________________________________________________________________________________________________ 
|    __         _    __    ___    _    __   __                          Possui:''',cursores,'''                           
|   /    |  |  |_)  (__   /   \  |_)  |__  (__                          Preço:''',int(v_cursores),'''                          
|   \__  |__|  |\    __)  \___/  |\   |__   __)                         Aumento:''',a_cursores,'''                          
|____________________________________________________________________________________________________________
|    __    _    ___    __   __   __   __    ___    _    __   __         Possui:''',professores,'''                           
|   |__)  |_)  /   \  |__  |__  (__  (__   /   \  |_)  |__  (__         Preço:''',int(v_professores),'''                          
|   |     |\   \___/  |    |__   __)  __)  \___/  |\   |__   __)        Aumento:''',a_professores,'''                          
|____________________________________________________________________________________________________________
|             _   ___   __            _   ___      __   ___    __       Possui:''',matematicos,'''                                   
|   |\  /|   /_\   |   |__  |\  /|   /_\   |   |  /    /   \  (__       Preço:''',int(v_matematicos),'''                     
|   | \/ |  /   \  |   |__  | \/ |  /   \  |   |  \__  \___/   __)      Aumento:''',a_matematicos,'''                          
|____________________________________________________________________________________________________________
|    __            _     __    _    ___    __                           Possui:''',quadros,'''                           
|   | _|   |  |   /_\   |  \  |_)  /   \  (__                           Preço:''',int(v_quadros),'''                          
|   |__|\  |__|  /   \  |__/  |\   \___/   __)                          Aumento:''',a_quadros,'''                          
|____________________________________________________________________________________________________________
|    __    _     __    _       __    _     __                           Possui:''', fabricas,'''                           
|   |__   /_\   |__)  |_)  |  /     /_\   (__                           Preço:''',int(v_fabricas),'''                          
|   |    /   \  |__)  |\   |  \__  /   \   __)                          Aumento:''',a_fabricas,'''                          
|____________________________________________________________________________________________________________
O evento raro aconteceu ''',{contador_de_eventos},''' vezes em ''',{numero_de_testes},''' testes.

''')

    
    elif menu == "melhorias":
        print('''\n\n\n\n\n\n\n\n
                                         __              ___    _        _     __
                                |\  /|  |__  |    |__|  /   \  |_)  |   /_\   (__
                                | \/ |  |__  |__  |  |  \___/  |\   |  /   \   __)

    Digite a letra e o numero ao lado da melhoria para compra-la
    Aperte "Enter" para voltar ao menu principal
 _______________________________________________________________________ ___________________________________ ___________________________________ ___________________________________ ___________________________________
|          Clique duplo-b1          |          Super clique-b2          |            Mega clique            |           Ultra clique            |          Clique supremo           |                                   |
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
              

Triângulos:
              
-Em breve
              

Renascimentos:
              
-Você pode renascer a qualquer momento do jogo, mas não ganhará nada enquanto não chegar à''',m_qua_as,''' 
de quadrados 

-Renascer fará com que você perca todos os seus quadrados, melhorias e construções

-Renascer te dará quadrados ascendentes, uma moeda que permitirá comprar melhorias durante o periodo de
renascimento, essas melhorias só podem ser compradas enquanto você estiver renascendo

-Para renascer digite "renascer" e depois aperte "enter", depois digite "confirmar" e aperte "enter"


''')
    
    elif menu == "renascer":
        print('''\n\n
              
                            _    __          _     __    __   __   _
                           |_)  |__  |\ |   /_\   (__   /    |__  |_)
                           |\   |__  | \|  /   \   __)  \__  |__  |\ 
              


-Ao renascer, você perderá todos os seus quadrados, contruções e melhorias, mas manterá seus triângulos
e quadrados ascendentes
              
-Você acessará uma tela que pode ser usada para comprar um tipo diferente de melhorias, chamadas de 
melhorias ascendentes
              
-Para comprar essas melhorias será necessario usar um tipo de moeda chamada de quadrados ascendentes

-Você começa a produzir quadrados ascendentes quando ultrapassa 100000000 de quadrados
              
-Você possui''',quadrados_ascendentes,'''quadrados ascendentes
              

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

Produtividade dobrada:
Dobra seus quadrados por clique
Preço:2 
              






''')

    elif menu == "salvar":
        print('''

digite salvar para salvar



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

        # Resultados
        print(f"O evento raro aconteceu {contador_de_eventos} vezes em {numero_de_testes} testes.")

    
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
    if algo == "confirmar" and menu == "renascer":
        quadrados = 0
        click_base = 1
        menu = "renascimento"

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

    if algo == "salvar":
        menu = "salvar"

    if algo == "salvarrr" and menu == "salvar":
        salvar_jogo()

    if algo == "carregar" and menu == "salvar":
        carregar_jogo()