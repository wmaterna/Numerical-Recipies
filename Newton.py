from numpy import zeros,array
from math import sqrt
from numpy import zeros,dot
from numpy import zeros
from numpy import argmax



def gaussPivot(a,b,tol=1.0e-9):
    n = len(b)
    s = zeros(n)
    for i in range(n):
        s[i] = max(abs(a[i,:]))
    for k in range(0,n-1):
        p = argmax(abs(a[k:n,k])/s[k:n]) + k
        if p != k:
            swap.swapRows(b,k,p)
            swap.swapRows(s,k,p)
            swap.swapRows(a,k,p)

        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a [i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

def newtonRaphson(f,x,tol=1.0e-9):

    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        return jac,f0
    for i in range(30):
        jac,f0 = jacobian(f,x)
        if sqrt(dot(f0,f0)/len(x)) < tol: return x
        dx = gaussPivot(jac,-f0)
        x = x + dx
        if sqrt(dot(dx,dx)) < tol*max(max(abs(x)),1.0): return x
    print ("Too many iterations")



def f(x):
    f = zeros(len(x))
    f[0] = 2*x[0]*x[0] + x[1]**2 -2.0
    f[1] = (x[0]-0.5)**2 + (x[1]-1)**2 - 0.25
    return f
x = array([1.0, 1.0])
x=newtonRaphson(f,x)
print("Solution vector [x,y]:")
print(x)
sol1=2*x[0]*x[0] + x[1]**2
sol2=(x[0]-0.5)**2 + (x[1]-1)**2
print("Check: ")
print("2*x^2+y^2=")
print(sol1)
print("(x-0,5)^2-(y-1)^2=")
print(sol2)
