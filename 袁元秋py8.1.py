"""
author:Yuan yuanqiu
function:函数拟合
date:2019.4.21
"""
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
params = dict(
fname = R"C:\Users\HUAWEI\Desktop\python\巨磁3.csv",#打开文件巨磁3.csv
delimiter = ',',
usecols = (0,1),

unpack = True
)
x,y= np.loadtxt(**params)

def func(x, A, k, theta):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """

    return A*np.sin(2*np.pi*k*x+theta)   
def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, A, k, theta)
popt, pcov = curve_fit(func, x, y)
# a=popt[0]#popt里面是拟合系数，读者可以自己help其用法
# b=popt[1]
A=50
k=1/22.08
theta=-np.pi/2.062
x1=np.arange(92, 141, 1)
yvals=func(x1,A,k,theta)
# plt.title("Giant magnetic effect")


plt.plot(x,y)
plot1=plt.plot(x, y, '*',label='Real Data')
plot2=plt.plot(x1, yvals, 'r',label='Fitting function')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')
plt.show()
plt.savefig('p2.png')
