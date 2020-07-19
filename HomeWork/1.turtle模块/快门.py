import turtle
import time

def drawline(x,y,n,l,s):        # n为线条重复次数，l为线条长度，s为内部多边形长度
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.lt(90)
    for i in range(1,n+1):
        turtle.fd(l)
        turtle.lt(180)
        turtle.fd(l-s)
        turtle.lt(180-360/n)
    turtle.ht()
    time.sleep(3)

drawline(10,20,8,150,30)