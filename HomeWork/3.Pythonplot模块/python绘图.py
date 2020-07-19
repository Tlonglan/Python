def func_sin(m,xlm):
    import matplotlib.pyplot as plt
    import numpy as np
    a = [] ; w = [] ; fi = []                                           #sin函数的3个参数
    c=['red','green','yellow','blue','orange','purple','black']   #绘制的函数图像的颜色

    plt.figure(figsize=(8,8))
    for i in range(0,m):
        print('请输入第',i+1,'个函数的各项参数：')
        A = float(input('振幅a：'));a.append(A)
        W = float(input('角频率w:'));w.append(W)
        F = float(input('初相位fi:'));fi.append(F)
        x=np.linspace(0,xlm,1000)
        y=np.sin(x*w[i]+fi[i])*a[i]
        plt.plot(x, y, c[i],label=('a=', a[i], 'w=', w[i], 'fi=', fi[i]), linewidth=2)
        plt.ylim(-a[i] - a[i] / 5, a[i] + a[i] / 5)

    plt.title("Test")
    plt.xlabel("x")
    plt.ylabel("y=a*sin(w*x+fi)")
    plt.legend()
    plt.show()

n=int(input('请输入需要绘制的函数的数量：'))
xl=float(input('请输入自变量最大值：'))
func_sin(n,xl)