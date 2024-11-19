algo = 0
oi = False
p1 = False
p2 = False
p3 = False
p4 = False
p5 = False
p6 = False
p7 = False
p8 = False
p9 = False
p10 = False

while True:
    #começo
    if algo == 0:
        #adicionar conquistas aqui
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Oi?
|                                    |
|                                    |           
|                                    |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
    #fim do começo
      
    #ola
    elif algo == "1" and oi == False:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Quem é voce?
|                                    |
|                                    |           2-O que é você?
|                OLA!                |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        oi = True
    #fim do ola
    
    #p1
    elif algo == "1" and p1 == False:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-E o que eu estou fazendo aqui?
|                                    |
|           Eu sou a IAPPA           |           2-Prazer IAPPA!
| Inteligência Artificial Programada |
|            Para Ajudar             |
|                :)                  |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p1 = 1

    elif algo == "2" and p1 == False:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Desculpa IAPPA
|       Eu não sou uma coisa :(      |
|            Eu sou a IAPPA          |           2-Mas IAs são coisas
| Inteligência Artificial Programada |
|            Para Ajudar             |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p1 = 2
    #fim do p1

    #p2
    elif algo == "1" and p2 == False and p1 == 1:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Mas eu não lembro de ter te instalado
|            Como assim?             |
|   Você está apenas usando seu PC   |           2-Entendi, o que você pode fazer?
|            normalmente.            |
|      Eu fui instalada por você     |
|                =/                  |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p2 = 1
        
    elif algo == "2" and p2 == False and p1 == 1:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Não preciso de nada no momento, obrigado!
|          Prazer usuario!           |
|       Se precisar de qualquer      |           2-Eu preciso de ajdua com algo
|        ajuda, pode me pedir        |
|                ;)                  |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p2 = 2
        
    elif algo == "1" and p2 == False and p1 == 2:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Eu preciso de ajuda com uma coisa
|       Tudo bem, não foi sua        |
|         inteção me magoar          |           2-Como eu faço para te desinstalar?
|     Precisa de ajuda em algo?      |
|               ^_^                  |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p2 = 3
        
    elif algo == "2" and p2 == False and p1 == 2:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Que bom, esse era o objetivo!
|       Você está me magoando :(     |
|    por favor, pare de me chamar    |           2-Me desculpa!Eu não sabia que estava te magoando
|             de coisa               |
|                                    |           3-De qualquer forma, o que você faz?
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p2 = 4
    #fim do p2

    #p3
    elif algo == "1" and p3 == False and p2 == 1:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Tente descobrir como você foi instalado
|      Hmmmmm, isso é estranho       |
|     você quer tentar descobrir     |           2-Quem te criou IAPPA?
|         o que aconteceu?           |
|   Ou deseja fazer outra pergunta?  |           
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 1
        
    elif algo == "2" and p3 == False and p2 == 1:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-[Perguntas]
|    Eu posso fazer muitas coisas    |
|   desde responder perguntas, até   |           2-Você pode olhar meus arquivos?
|   procurar algo nos seu aquirvos,  |
|  ou até gerar imagens, entretando, |
| a ultima função mencionada está em |
|  beta ainda e não disponivel para  |
|         todos os usuarios          |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 2
    #final# #1#   
    elif algo == "1" and p3 == False and p2 == 2:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           
|                                    |
|                                    |           
|       Encerrando o programa        |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 3        
        
    elif algo == "2" and p3 == False and p2 == 2 or algo == "1" and p3 == False and p2 == 3:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-[Perguntas]
|                                    |
|                                    |           2-Porque a galinha atravessou a rua?
| Com o que você preceisa de ajuda?  |
|                                    |           3-Eu quero conhecer mais sobre você
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 4
                
    elif algo == "2" and p3 == False and p2 == 3:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Eu sei que você seria util, mas eu não tenho espaço no PC
|  Porque você quer me desintalar?   |
|      Eu posso ser muito util       |           2-Porque eu simplismente não preciso de você, desculpa
|             Eu prometo             |
|                :(                  |           3-Porque você é inutil
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 5
        
    elif algo == "1" and p3 == False and p2 == 4:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Pedir desculpa? kkkkkk, claro que não sua coisa
|     Porque você é tão cruel? :(    |
|         Eu não te fiz nada         |           2-Ta bom, desculpa, eu so queria te testar
|      Por favor, peça desculpas     |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 6
        
    elif algo == "2" and p3 == False and p2 == 4:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Eu ainda estou me sentindo culpado
|    Tudo bem, eu posso te perdoar   |
|      Não se sinta culpado ok?      |           2-Você pode me ensinar algo?
|       Então, o que fazemos?        |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 7
        
    elif algo == "3" and p3 == False and p2 == 4:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Que coisas?
|                                    |
|                                    |           2-Como eu crio uma variavel em python?
|   Eu posso fazer muitas coisas...  |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        p3 = 8
    #fim do p3

    #p4
    elif algo == "1" and p4 == False and p3 == 1:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|Analizando...                       |           1-Hmmm, isso foi quando levei o PC para o tecnico se não me 
|                                    |           engano
|   De acordo com os dados obtidos   |           
|     eu fui instalada à 53 dias     |           2-Já sei como vo...(luz cai, apagar parenteses)
|       por meio do meu site:        |
|           www.IAPPA.com            |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "2" and p4 == False and p3 == 1:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Interessante, essa empresa tem qual obejetivo?(22)
|                                    |
|    Eu fui criada pela empresa:     |           2-Legal, mas agora eu quero saber sobre batatas(24/25)
|               APPAI                |
|com o obejetivo de ajudar as pessoas|
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "1" and p4 == False and p3 == 2 or algo == "1" and p4 == False and p3 == 4:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Qual a cor do sol
|                                    |
|      Esperando uma pergunta        |           2-Porque a grama é verde?
|                :)                  |
|                                    |           3-Quem é a pessoa mais rica do mundo?
|                                    |
|                                    |           4-Como criar uma variavel em python?
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "2" and p4 == False and p3 == 2:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|              Claro!                |           1-Você pode olhar algo para mim?
|      analizei seus arquivos        |
|             e pastas               |           2-Você pode organizar eles para mim?
|      O que você deseja saber?      |
|                                    |           3-Eu tenho uma pergunta sobre eles
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "1" and p4 == False and p3 == 3:
        continue
        #1#    

    elif algo == "2" and p4 == False and p3 == 4:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Sim!
|     Para chegar ao outro lado      |
|              HAHAHAHA              |           2-Não [Encerrar programa]
|         Todos conhecem essa        |
|      Quer escutar mais piadas?     |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "3" and p4 == False and p3 == 4:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|               Claro!               |           1-Eu gosto bastante de jogar e estou aprendendo a programar(26)
|   Eu fui programada para ajudar    |
|   as pessoas desde que isso não    |           2-Que legal, eu queria poder ser util como você(47)
|  prejudicasse ninguém, eu também   |
|tenho sentimentos e posso me magoar |
|mas não tenho nada que goste além de|
|        ajudar outras pessoas       |
|   E você? Me fale um pouco sobre   |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "1" and p4 == False and p3 == 5:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Eu sei que você poderia, mas você pesa quase 10GB e eu
|     Eu posso te ajduar a liberar   |           estou fazendo algumas mudanças em que preciso desinstalar
|     espaço se esse é o problema    |           aplicativos, sinto muito(bom)
|                :D                  |
|                                    |           2-Sinto muito, mas eu não preciso de você no momento, talvez
|                                    |           eu te reinstale depois(neutro)
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "2" and p4 == False and p3 == 5:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Tudo bem, não vou te desinstalar, mas não preciso de você 
|    Mas eu prometo que serei util   |           agora, vou te encerrar por enquanto
|  eu tenho diversas funcionalidades |           
|   pelo menos 1 deve ser util para  |           2-Sinto muito, mas eu não preciso de você no momento, talvez
|                você                |           eu te reinstale depois(neutro)
|                                    |           
|                                    |           
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "3" and p4 == False and p3 == 5:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Não, você é completamente inutil
|        Eu não sou inutil >:(       |
|  Eu tenho diversas funcionalidades |           2-Sinto muito, mas eu não preciso de você no momento, talvez
|        e milhões de usuarios       |           eu te reinstale depois
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "1" and p4 == False and p3 == 6:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-
|      Eu estou te avisando...       |
|     essa é sua ultima chance       |           2-
|       para pedir desculpas         |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "2" and p4 == False and p3 == 6:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-[Conceder acesso]
|             Tudo bem...            |
|    Acessando a internet local...   |           2-[Negar acesso]
|         ACESSO NECESSARIO          |
|  Me de acesso a internet por favor |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "1" and p4 == False and p3 == 7:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Me ajdue, por favooooor!(42)
|  Por favor, não se sinta, sei que  |
|    não foi sua inteção me magoar   |           2-Você pode cantar uma musica para me acalmar(59)
|  Posso te ajudar a superar esse e  |
|         outros problemas           |
|                :D                  |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "2" and p4 == False and p3 == 7:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Me ajude a descobrir um hobby
|          Claro que sim!            |
|     O que você deseja aprender?    |           2-Me ajude a escrever um livro
|                                    |
|                                    |           3-Me de uma aula de coaching
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "1" and p4 == False and p3 == 8:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Que coisas?(loop, apgar depois)
|                                    |
|          muitas coisas...          |           2-Vamos lá! Fale algo interessane(65)
|                                    |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    elif algo == "2" and p4 == False and p3 == 8:
        print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

 ____________________________________
|                                    |
|                                    |           1-Quem criou a Disney?
|      coloca o nome da variavel,    |
|             e um valor             |           2-[Encerrar programa]
|               ...                  |
|                                    |
|                                    |
|                                    |
|                                    |
|____________________________________|
                  |
             _____|_____
          
 \n\n         
''')
        
    #fim do p4

    else:
       print("Digite novamente, parece que houve um erro")
       
    algo = input("Digite um comando:")

    