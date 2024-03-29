import turtle
import time

def drawcross10(x,y,l,s,n):       # n为条形数量，l为条形长度，s为条形宽度
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.speed(4)

    for i in range(1,n+1):
        turtle.fd(l)
        turtle.rt(90)
        turtle.fd(s)
        turtle.rt(90)
        turtle.fd(l)
        turtle.lt(360/n)
    time.sleep(3)
    turtle.ht()

drawcross10(10,20,90,30,8)