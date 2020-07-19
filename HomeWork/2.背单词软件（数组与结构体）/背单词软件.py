def recite(n):
    #词典，元组结构为{单词：释义}
    dict = {
        "horse": "马",
        "stallion": "雄马",
        "mare": "雌马",
        "foal": "幼马",
        "colt": "幼马",
        "filly": "幼马",
        "gelding": "阉割的马",
        "coordinate": "坐标系",
        "particle": "粒子",
        "wave": "波",
        "energy": "能量",
        "momentum": "动量",
        "uncertainty": "不确定性",
        "quantum": "量子",
        "cattle": "牛",
        "bull": "雄牛",
        "ox": "雄牛",
        "cow": "雌牛",
        "calf": "年幼的牛",
        "water buffalo": "水牛",
        "yak": "牦牛",
        "sheep": "绵羊",
        "ram": "雄绵羊",
        "ewe": "雌绵羊",
        "lamb": "年幼的绵羊",
        "flock": "绵羊的统称",
        "mutton": "羊肉",
        "goat": "山羊",
        "billy": "雄山羊",
        "nanny": "雌山羊",
        "kid": "年幼的山羊",
        "pig": "猪",
        "boar": "雄猪",
        "sow": "雌猪",
        "piglet": "年幼的猪",
        "shoat": "年幼的猪",
        "herd": "猪的统称",
        "mechanics ": "力学",
        "thermotics": "热学",
        "electromagnetics": "电磁学",
        "optics": "光学"
    }

    import random
    word = list(dict.keys())  #将词典中的所有单词提取到一个列表中，以便后面随机生成测试单词
    ran = []  # 存放已生成的随机数，以便后面进行排除
    m = 0  #猜对单词的个数
    # 该循环生成不重复的单词并用于检测
    for j in range(0, n):
        # 该循环生成不重复的随机数
        while (1):
            w = int(random.random() * 10)  #生成随机数
            if w in ran:
                continue
            else:
                ran.append(w)
                wlist = word[w]  #生成随机单词
                break
        print(wlist)
        ep = input('请输入该单词的意义：')
        if ep == dict[wlist]:
            print("Right")
            m = m + 1
        else:
            print("Error")
    p = (m / n) * 100  #正确率
    print("此次单词背诵的正确率为", p, "%")


#背单词小程序
while (1):
    n = int(input('请输入想测试的单词数量：'))  #测试单词的数量
    recite(n)
    print("是否继续背单词？要继续请输入“Y”，退出请输入“N”")
    A = input()
    if (A == 'Y'):
        continue
    if (A == 'N'):
        exit()