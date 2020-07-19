dict={"horse":"马",
     "stallion":"雄马","mare":"雌马", "foal":"幼马","colt":"幼马","filly":"幼马","gelding":"阉割的马",

     "coordinate":"坐标系","particle":"粒子","wave":"波","energy":"能量","momentum":"动量","uncertainty":"不确定性","quantum":"量子",

    "cattle":"牛","bull":"雄牛","ox":"雄牛","cow":"雌牛","calf":"年幼的牛","water buffalo":"水牛","yak":"牦牛",

    "sheep":"绵羊","ram":"雄绵羊","ewe":"雌绵羊","lamb":"年幼的绵羊","flock":"绵羊的统称","mutton":"羊肉",

    "goat":"山羊","billy":"雄山羊", "nanny":"雌山羊","kid":"年幼的山羊",

    "pig":"猪","boar":"雄猪","sow":"雌猪","piglet":"年幼的猪","shoat":"年幼的猪","herd":"猪的统称",

    "mechanics ":"力学","thermotics":"热学","electromagnetics":"电磁学","optics":"光学"
    }

import random
list=[]
for i in range(0,5):
    w=int(random.random()*10)
    if (i==0):list[i]=w
    if(i>0):
        for j in  range(0,i+1):
            if(w!=list[j]):
                list[j+1] = w
            break

list=[1,2,3,4,5]
for i in range(1,3):
    list[i]=list[i]+5
    print(list[i])

# d=list(dict.keys())