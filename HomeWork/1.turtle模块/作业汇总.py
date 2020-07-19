import turtle
import time

#条状花瓣绘制函数
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

#内置星型的n变形绘制函数
def drawcross8(x,y,l,n):       # l为多边形边长,n为锐角数
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.speed(n)
    for i in range(1,int((n+1)/2)+1):
        turtle.lt(360 / n)
        turtle.fd(l)
        turtle.rt(720/n)
        turtle.fd(l)
        turtle.rt(180 - 360 / n)
        turtle.fd(l)
        turtle.rt(360/n)
        turtle.fd(l)
        turtle.rt(180 - 360 / n)
        turtle.fd(l)
        turtle.rt(720/ n)
        turtle.fd(l)
    turtle.ht()
    time.sleep(2)

#旗子绘制函数
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

#三角形环状排列绘制函数
def drawtri(x,y,s,l,n):     # s为三角形边长，l为内部多边形边长，n为三角形重复次数
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

#快门绘制函数
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

#八边形条状十字绘制函数
def drawcross10(x,y,l,s):       # l为条形长度，s为条形宽度
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()
    turtle.speed(4)

    for i in range(1,9):
        turtle.fd(l)
        turtle.rt(90)
        turtle.fd(s)
        turtle.rt(90)
        turtle.fd(l)
        turtle.lt(45)
    time.sleep(3)
    turtle.ht()

drawrectan(0,0,30,10,10)
drawcross8(120,-10,30,8)
drawflag(250,-25,25,3,5)
drawtri(20,-200,25,15,8)
drawline(120,-180,8,50,10)
drawcross10(250,-160,30,10)
