import turtle
import time

def drawcross(x,y,l,s,n):       # l为多边形边长，s为多边形边宽,n为锐角数
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.speed(1)

    for i in range(1,int((n+1)/2)+1):
        turtle.lt(360 / n)
        turtle.fd(l)
        turtle.rt(90)
        turtle.fd(s)
        turtle.rt(90)
        turtle.fd(l)
        turtle.rt(360/n)
        turtle.fd(l)
        turtle.rt(90)
        turtle.fd(s)
        turtle.rt(90)
        turtle.fd(l)

    turtle.ht()
    time.sleep(2)

drawcross(10,20,60,20,8)