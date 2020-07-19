import turtle
import time

def drawflag(x,y,l,t,n):      # l,t为旗子边长,旗子边数,n为旗子数量
    turtle.speed(n)
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.lt(90)

    for i in range(1,n+1):
        turtle.fd(2*l)
        for j in range(1,t):
            turtle.rt(360/t)
            turtle.fd(l)
        turtle.lt(180/t+180-360/n)
    turtle.ht()
    time.sleep(2)

drawflag(10,20,100,3,8)
