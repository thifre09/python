import turtle

cubond = {"cubo3":
    [
    (0,0),
    (100,0),
    (100,100),
    (0,100),
    (0,0),
    (-50,50),
    (50,50),
    (100,0),
    (50,50),
    (50,150),
    (100,100),
    (50,150),
    (-50,150),
    (0,100),
    (-50,150),
    (-50,50)
    ]
}

def tele(local):
    global p
    p.penup()
    p.goto(local)
    p.pendown()


p = turtle.Turtle()
p.hideturtle()
p.speed(0)

def cubo(dimensões):
    global p, cubond

    x = 0
    y = 0

    if dimensões == 1:
        p.goto(0,100)

    elif dimensões == 2:
        p.goto(100,0)
        p.goto(100,100)
        p.goto(0,100)

    elif dimensões >= 3:
        pass
            

    p.goto(0,0)

cubo(1)
turtle.done()