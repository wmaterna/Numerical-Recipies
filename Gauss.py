import numpy
from numpy import zeros
from numpy import dot
from math import sqrt

def iter (x, omega):
   n = len(x)
   tmp=x.copy()
   x[0] = omega*(1.0-x[1]- x[4])/4.0 + (1.0 - omega)*x[0]
   for i in range(1,4):
       x[i]=omega*(1.0-x[i-1]-x[i+1]-x[i+4])/4.0 + (1.0 - omega)*x[i]
   for i in range(4,n-4):
       x[i] = omega*(1-x[i-1]-x[i+1]-x[i-4]-x[i+4])/4.0 + (1.0 - omega)*x[i]
   for i in range(n-4,n-1):
       x[i] = omega*(1-x[i-1]-x[i+1]-x[i-4])/4.0 + (1.0 - omega)*x[i]
   x[n-1] = omega*(1.0 - x[n-5] - x[n-2])/4.0 + (1.0 - omega)*x[n-1]

   return x


def gaussSeidel(iter,x,tol = 1.0e-9):
   omega = 1.0
   k = 10
   p=1
   for i in range(1,501):
       xOld = x.copy()
       x= iter(x,omega)
       dx = sqrt(dot(x-xOld,x-xOld))
       if dx < tol: return x,i,omega

       if i == k: dx1 = dx
       if i == k + p:
           dx2 = dx
           tmp=(dx2/dx1)**(1.0/p)
           omega = 2/(1.0 + sqrt(1.0 - ((dx2/dx1)**(1.0/p))))
   print ("Gauss-Seidel failed to converge’")

n = eval(input("Number of equations ==> "))
x = zeros(n)
print("Norms:")
x,numIter,omega= gaussSeidel(iter,x)
print ("\nNumber of iterations =",numIter)
print ("\nRelaxation factor =",omega)
print ("\nThe solution is:\n",x)

