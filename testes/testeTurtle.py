import turtle
import random

# Configuração da tela
screen = turtle.Screen()
screen.title("Colete a Estrela!")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Tartaruga do jogador
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Estrela (como um círculo)
star = turtle.Turtle()
star.shape("circle")
star.color("yellow")
star.penup()
star.speed(0)
star.goto(random.randint(-290, 290), random.randint(-290, 290))

# Variável para contar pontos
score = 0

# Função para mover a tartaruga
def move_up():
    if player.ycor() < 250:  # Limite superior
        y = player.ycor()
        player.sety(y + 20)

def move_down():
    if player.ycor() > -250:  # Limite inferior
        y = player.ycor()
        player.sety(y - 20)

def move_left():
    if player.xcor() > -250:  # Limite esquerdo
        x = player.xcor()
        player.setx(x - 20)

def move_right():
    if player.xcor() < 250:  # Limite direito
        x = player.xcor()
        player.setx(x + 20)

# Função para checar colisão
def check_collision():
    global score
    if player.distance(star) < 20:
        score += 1
        print(f"Pontos: {score}")
        star.goto(random.randint(-290, 290), random.randint(-290, 290))

# Função para fechar o jogo
def exit_game():
    screen.bye()

# Controles do jogador
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(exit_game, "q")  # Pressione "q" para sair do jogo

# Loop principal do jogo
while True:
    screen.update()
    check_collision()

# Manter a tela aberta
turtle.done()
