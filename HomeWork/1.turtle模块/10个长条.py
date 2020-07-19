import turtle
import time

def drawrectan(ori_x,ori_y,l,s,n):        #ori_x,ori_y 为起始画点，l，s，n分别为条形长度，宽度，重复数量
    turtle.speed(n)
    turtle.pu()
    turtle.setpos(ori_x, ori_y)
    turtle.pd()
    turtle.lt(90)
    for i in range (1,n+1):
        turtle.speed(3)
        turtle.fd(l)                #向上（y）前进
        turtle.rt(90)
        turtle.fd(s)
        turtle.rt(90)
        turtle.fd(l)
        turtle.lt(180-360/(n))
    turtle.ht()
    time.sleep(2)

drawrectan(0,0,60,20,10)