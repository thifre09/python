import turtle
import random
import time

screen = turtle.Screen()
screen.title("Colete a Estrela!")
screen.bgcolor("lightblue")
screen.setup(width=2000, height=1000)

# Jogador 1
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

def cima():
    if player.ycor() < 480:
        player.setheading(90)
        player.forward(30)

def baixo():
    if player.ycor() > -480:
        player.setheading(270)
        player.forward(30)

def esquerda():
    if player.xcor() > -920:
        player.setheading(180)
        player.forward(30)

def direita():
    if player.xcor() < 920:
        player.setheading(0)
        player.forward(30)

# Jogador 2
player2 = turtle.Turtle()
player2.shape("turtle")
player2.color("blue")
player2.penup()
player2.speed(0)

def cima2():
    if player2.ycor() < 480:
        player2.setheading(90)
        player2.forward(30)

def baixo2():
    if player2.ycor() > -480:
        player2.setheading(270)
        player2.forward(30)

def esquerda2():
    if player2.xcor() > -920:
        player2.setheading(180)
        player2.forward(30)

def direita2():
    if player2.xcor() < 920:
        player2.setheading(0)
        player2.forward(30)

def perdeu():
    global p1_pontos,p2_pontos
    for inimigo in inimigos:
        if player.distance(inimigo) < 30:
            print("Player 1 morreu")
            screen.bye()  # Encerra o jogo
            p1_pontos -= 3
            print(f"""
            Pontos do player 1: {p1_pontos}
            Pontos do player 2: {p2_pontos}
            """)
        elif player2.distance(inimigo) < 30:
            print("Player 2 morreu")
            screen.bye()  # Encerra o jogo
            p2_pontos -= 3
            print(f"""
            Pontos do player 1: {p1_pontos}
            Pontos do player 2: {p2_pontos}
            """)

# Criação inicial dos inimigos
inimigos = []
def adicionar_inimigo():
    while True:
        # Posiciona aleatoriamente
        x = random.randint(-920, 920)
        y = random.randint(-480, 480)
        novo_inimigo = turtle.Turtle()
        novo_inimigo.shape("turtle")
        novo_inimigo.color("red")
        novo_inimigo.penup()
        novo_inimigo.speed(0)
        novo_inimigo.setpos(x, y)

        # Verifica a distância dos jogadores
        if player.distance(novo_inimigo) > 150 and player2.distance(novo_inimigo) > 150:
            inimigos.append(novo_inimigo)
            break  # Sai do loop se o novo inimigo estiver longe o suficiente
        if player.distance(novo_inimigo) < 150 and player2.distance(novo_inimigo) < 150:
            novo_inimigo.hideturtle()

# Adiciona o primeiro inimigo
adicionar_inimigo()

def mover_inimigo(inimigo:turtle):
    direcao = random.randint(1, 4)
    if direcao == 1:
        if inimigo.ycor() < 480:
            inimigo.setheading(90)
            inimigo.forward(30)
    elif direcao == 2:
        if inimigo.ycor() > -480:
            inimigo.setheading(270)
            inimigo.forward(30)
    elif direcao == 3:
        if inimigo.xcor() > -920:
            inimigo.setheading(180)
            inimigo.forward(30)
    elif direcao == 4:
        if inimigo.xcor() < 920:
            inimigo.setheading(0)
            inimigo.forward(30)


last_add_time_poder1 = time.time()
poderes1 = []

p1_poderes1 = 0
p2_poderes1 = 0
def adicionar_poder1():
    while True:
        # Posiciona aleatoriamente
        x = random.randint(-920, 920)
        y = random.randint(-480, 480)
        novo_poder = turtle.Turtle()
        novo_poder.shape("circle")
        novo_poder.color("black")
        novo_poder.penup()
        novo_poder.speed(0)
        novo_poder.setpos(x, y)

        # Verifica a distância dos jogadores
        if player.distance(novo_poder) > 150 and player2.distance(novo_poder) > 150:
            poderes1.append(novo_poder)  # Adiciona à lista de poderes
            break  # Sai do loop se o novo poder estiver longe o suficiente

def checar_poder():
    global p1_poderes1, p2_poderes1
    for poder in poderes1:  # Use uma cópia da lista para evitar modificações durante a iteração
        if player.distance(poder) < 40:
            poder.hideturtle()  # Esconde o poder
            poder.setpos(10000,10000)
            p1_poderes1 += 1
            poderes1.remove(poder)  # Remove o poder da lista
        if player2.distance(poder) < 40:
            poder.hideturtle()  # Esconde o poder
            poder.setpos(10000,10000)
            p2_poderes1 += 1
            poderes1.remove(poder)  # Remove o poder da lista

def p1_usar_poder1():
    global p1_poderes1
    if p1_poderes1 >= 1:
        for inimigo in inimigos:
            if player.distance(inimigo) <= 200:
                inimigo.setpos(10000,10000)

def p2_usar_poder1():
    global p2_poderes1
    if p2_poderes1 >= 1:
        for inimigo in inimigos:
            if player2.distance(inimigo) <= 200:
                inimigo.setpos(10000,10000)

last_add_time_pontos = time.time()
pontos = []

p1_pontos = 0
p2_pontos = 0
def adicionar_pontos():
    while True:
        # Posiciona aleatoriamente
        x = random.randint(-920, 920)
        y = random.randint(-480, 480)
        novo_ponto = turtle.Turtle()
        novo_ponto.shape("circle")
        novo_ponto.color("yellow")
        novo_ponto.penup()
        novo_ponto.speed(0)
        novo_ponto.setpos(x, y)

        # Verifica a distância dos jogadores
        if player.distance(novo_ponto) > 150 and player2.distance(novo_ponto) > 150:
            pontos.append(novo_ponto)  # Adiciona à lista de poderes
            break  # Sai do loop se o novo poder estiver longe o suficiente

def checar_pontos():
    global p1_pontos, p2_pontos
    for ponto in pontos:
        if player.distance(ponto) < 40:
            ponto.hideturtle()  # Esconde o poder
            p1_pontos += 1
            ponto.setpos(10000,10000)

        elif player2.distance(ponto) < 40:
            ponto.hideturtle()  # Esconde o poder
            p2_pontos += 1
            ponto.setpos(10000,10000)
    

# Variáveis de controle
last_move_time = time.time()
move_delay = 1  # Tempo em segundos para o movimento dos inimigos
last_add_time = time.time()  # Para adicionar inimigos

screen.listen()
# Controles do jogador 1
screen.onkey(cima, "w")
screen.onkey(baixo, "s")
screen.onkey(esquerda, "a")
screen.onkey(direita, "d")
screen.onkey(p1_usar_poder1,"space")

# Controles do jogador 2
screen.onkey(cima2, "Up")
screen.onkey(baixo2, "Down")
screen.onkey(esquerda2, "Left")
screen.onkey(direita2, "Right")
screen.onkey(p2_usar_poder1,"Return")

while True:
    try:
        screen.update()
        current_time = time.time()
        
        # Verifica se é hora de mover os inimigos
        if current_time - last_move_time >= move_delay:
            for inimigo in inimigos:
                mover_inimigo(inimigo)
            last_move_time = current_time
            
        # Verifica se é hora de adicionar um novo inimigo
        if current_time - last_add_time >= 5:
            adicionar_inimigo()
            last_add_time = current_time
        
        if current_time - last_add_time_pontos >= 3:
            adicionar_pontos()
            last_add_time_pontos = current_time

        if current_time - last_add_time_poder1 >= 20:
            adicionar_poder1()
            last_add_time_poder1 = current_time

        checar_poder()   
        checar_pontos() 
        perdeu()
    except turtle.Terminator:
        break
