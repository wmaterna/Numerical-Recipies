import numpy as np
import scipy
import matplotlib.pyplot as plt
import math

from scipy.interpolate import lagrange
from numpy import array,arange

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

def Lagrange(x,X):
    T = np.zeros((2,len(X)))
    list = []
    for i in range(len(X)):
        for j in range(len(X)):
            if i != j:
                list.append((x-X[j][0])/(X[i][0]-X[j][0]))
    p = []
    for i in chunkIt(list,len(X)):
        p.append(product(i))
    for i in range(len(X)):
        T[0][i] = p[i]
        T[1][i] = X[i][1]

    list2 = []
    for i in range(len(X)):
        list2.append(T[0][i]*T[1][i])
    return sum(list2)

def p(x, a):
    sum = 0
    for i in range(8):
        sum += a[i]*pow(x, i)
    return sum

points=[[0.062500,0.687959],[0.187500,0.073443],[0.312500,-0.517558],[0.437500,-1.077264],[0.562500,-1.600455],[0.687500,-2.080815],[0.812500,-2.507266],[0.937500,-2.860307]]
X=[0.062500,0.187500,0.312500,0.437500,0.562500,0.687500,0.812500,0.937500]
Y=[0.687959,0.073443,-0.517558,-1.077264,-1.600455,-2.080815,-2.507266,-2.860307]
order=len(points)
equations = np.array([[point[0] ** i for i in range(order)] for point in points])
values = np.array([point[1] for point in points])
coefficients = np.linalg.solve(equations, values)
print ("Coefficients:")
print(list(coefficients))
a=np.copy(coefficients)
for i in range (0,order):
    print("x ^",i,round(coefficients[i],4))
plt.scatter(X, Y, c='k')
xx = np.linspace(-1, 1, endpoint=True)
plt.plot(xx, p(xx, a) , linestyle=':')
plt.axhline(linewidth=1, color='b')
plt.axvline(linewidth=1, color='b')
plt.grid(True)
plt.show()
plt.savefig('wykres_wielomianu_interpolacyjnego.png')
for i in range(len(a)):
    print("a%i = %.4f" %(i, a[i]))


