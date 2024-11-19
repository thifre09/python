import turtle

zoom = 1
x = 0
y = 0

p = turtle.Turtle()


def go(num1,num2, zoom = zoom):
    global x,y
    p.goto(zoom * num1 + x, zoom * num2 + y)

def cubo_4d():
    p.pendown()
    p.speed(5)
    go(0,0)
    go(100,0)
    go(100,100)
    go(0,100)
    go(0,0)
    go(-50,50)
    go(50,50)
    go(100,0)
    go(50,50)
    go(50,150)
    go(100,100)
    go(50,150)
    go(-50,150)
    go(-50,50)
    go(-50,150)
    go(0,100)
    go(0,0)

    go(200,100)

    go(300,100)
    go(300,200)
    go(200,200)
    go(200,100)
    go(150,150)
    go(250,150)
    go(300,100)
    go(250,150)
    go(250,250)
    go(300,200)
    go(250,250)
    go(150,250)
    go(150,150)
    go(150,250)
    go(200,200)

    go(0,100)
    go(100,100)
    go(300,200)
    go(300,100)
    go(100,0)
    go(50,50)
    go(250,150)
    go(250,250)
    go(50,150)
    go(-50,150)
    go(150,250)
    go(150,150)
    go(-50,50)
    p.penup()
    go(0,0)

def ligações_5d():
    pass

def cubo_5d():
    global zoom,x,y,p
    cubo_4d()

    x = 100
    y = -200

    cubo_4d()



cubo_5d()
turtle.done()