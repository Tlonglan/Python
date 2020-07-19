import turtle
import time

def drawtri(x,y,s,l,n):     # n为三角形重复次数，s为三角形边长，l为内部多边形边长
    turtle.speed(n)
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.lt(60)
    for i in range(1,n+1):
        turtle.fd(s)
        turtle.rt(120)
        turtle.fd(s)
        turtle.rt(120)
        turtle.fd(s)
        turtle.lt(360/n)
        turtle.fd(l)
        turtle.rt(120)
    turtle.ht()
    time.sleep(3)

drawtri(10,20,100,75,6)