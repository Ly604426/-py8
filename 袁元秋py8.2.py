"""
author:Yuan yuanqiu
function:函数拟合
date:2019.4.21
"""
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
import matplotlib as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
x=np.arange('2018-01-01','2019-01-01',dtype='datetime64[M]')
print(x)
y=[17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
y1=[-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
pl.plot(x,y,"*",label="Maximum temperature")
pl.plot(x,y1,"*",label="Minimum temperature")
pl.plot(x,y)
pl.plot(x,y1)
pl.xlabel('x axis')
pl.ylabel('y axis')
pl.show()
pl.savefig('p2.png')