import numpy as np
pi = np.pi
E = 2.718

fun = input('请输入以 x 为未知量的单调代数式，如" x + 3 " \n')
a = float(input('请输入左区间:\n'))
b = float(input('请输入右区间:\n'))
e = float(input('请输入求解精度:\n'))

def f(x):                           #  变量 x 限制用户输入的未知量一定是 x
    return ( eval(fun) )            # 将输入的字符串转成可计算的代数式
def result(a,b):
    if (f(a) * f(b) > 0):
        print('方程',fun, '在区间[',a,',',b,']内无解')
    if (f(a) * f(b) == 0):
        if(f(a) == 0):
            print('result = ', a)
        if (f(b) == 0):
            print('result = ', b)
    if (f(a) * f(b) < 0):                # 二分法条件
        while(True):                    # 二分法步骤
            m = (a + b) / 2
            if (abs(a - b) < e):
                print('result = ',(a+b)/2)
                break
            if (abs(a - b) > e):
                if(f(a) * f(m) <= 0):
                    b = m
                if(f(m) * f(b) <= 0):
                    a = m

result(a,b)