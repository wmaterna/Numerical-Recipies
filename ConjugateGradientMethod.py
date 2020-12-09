import numpy
import numpy as np
from numpy import dot
from math import sqrt
from numpy import zeros,sqrt

def Ax(v):
    n = len(v)
    tmp=v.copy()
    Ax = zeros(n)
    Ax[0]=4.0*v[0] + v[1] + v[4]
    for i in range(1, 4):
        Ax[i] = v[i] * 4.0 + v[i - 1] + v[i + 1] + v[i + 4]
    for i in range(4, n - 4):
        Ax[i] =v[i] * 4.0+v[i - 1] + v[i + 1] + v[i - 4] + v[i + 4]
    for i in range(n - 4, n - 1):
        Ax[i] = v[i] * 4.0+ v[i - 1] + v[i + 1] + v[i - 4]
    Ax[n - 1] = v[n - 1] * 4.0 + v[n - 5] + v[n - 2]
    return Ax


def conjGrad(Av,x,b,tol=1.0e-9):
    n = len(b)
    r = b - Av(x)
    s = r.copy()
    for i in range(n):
        u = Av(s)
        alpha = dot(s,r)/dot(s,u)
        x = x + alpha*s
        r = b - Av(x)
        if(sqrt(dot(r,r))) < tol:
            break
        else:
            beta = -dot(r,u)/dot(s,u)
            s = r + beta*s
    return x,i

n = eval(input("Number of equations ==> "))
b = numpy.ones(128)
x = zeros(n)
x,numIter = conjGrad(Ax,x,b)
print ("\nThe solution is:\n",x)
print ("\nNumber of iterations =",numIter)
