import numpy as np
import scipy
import matplotlib.pyplot as plt
import math

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
def f(x):
    denominator=((x**2)*5)+1
    return 1/denominator

def x_creator(X):
    value1=-1.0
    for i in range (0,65):
        tmp=value1+(i*(1.0/32.0))
        X[i]=tmp
    return X

X=np.zeros(65)
Y=np.zeros(65)
X=x_creator(X)
points=np.zeros((65,2))
for i in range(0,65):
    points[i][0]=X[i]
for i in range(0,65):
    points[i][1]=f(X[i])
    Y[i]=points[i][1]

print("Points of given function:")
print(points)

order=len(points)
equations = np.array([[point[0] ** i for i in range(order)] for point in points])
values = np.array([point[1] for point in points])
coefficients = np.linalg.solve(equations, values)
a=np.copy(coefficients)
for i in range (0,order):
    print("x ^",i,coefficients[i])

plt.scatter(X, Y, c='k')
xx = np.linspace(-1, 1, endpoint=True)
yy = np.linspace(0, 1, endpoint=True)
plt.grid(True)
plt.show()
plt.savefig('wykres_wielomianu_interpolacyjnego2.png')


