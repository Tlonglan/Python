import turtle
import time

def drawcross8(x,y,l,n):       # l为多边形边长,n为锐角数
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.speed(n)

    # for i in range(1,int((n+1)/2)+1):
    #     turtle.lt(360 / n)
    #     turtle.fd(l)
    #     turtle.rt(720/n)
    #     turtle.fd(l)
    #     turtle.rt(180 - 360 / n)
    #     turtle.fd(l)
    #     turtle.rt(360/n)
    #     turtle.fd(l)
    #     turtle.rt(180 - 360 / n)
    #     turtle.fd(l)
    #     turtle.rt(720/ n)
    #     turtle.fd(l)
    for i in range(1,n):
        for j in range(1,3):
            turtle.fd(l)
            turtle.rt(180-360/n)
            turtle.fd(l)
            turtle.lt(360/n)

    turtle.ht()
    time.sleep(2)

drawcross8(10,20,60,8)