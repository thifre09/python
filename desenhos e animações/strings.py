from time import sleep
import turtle

titulo = "Patolino, o Mago"
letra = """Contemplem o mago
Com seus poderes
Incríveis poderes
Sob o olhar do necromante
A escada prateada vai se erguer
As pessoas maravilhadas
Com seus olhos cheios de poder
Comida fria vai esquentar ao enfeitiçar
Balançando as suas mãos
O cachorro quente explodirá
Na presença do grande mago
O trânsito para de repente
Pode atravessar a rua
Com os carros parados na sua frente
Na TV mudam-se os canais
Sem que saia do sofá
Sua varinha pega então
Pra reclinar-se no ar

Faminto por causa da última missão
O mago quer lanchar
Traça o rumo do prazer
Para o habitual lugar
Ele é o mago
O místico mago"""

turtle.addshape("python/atividades/kratos.gif")
k = turtle.Pen()
k.shape("python/atividades/kratos.gif")

p = turtle.Pen()
p.goto(200,300)
p.hideturtle()

for linha in letra.split("\n"):
    print(linha)
    p.write(linha)
    sleep(2.5)
    p.clear()
    

turtle.done()