import numpy
import numpy as np
import math

def ortho(z,v):
    tmp=0
    for i in range(0,len(z)):
        tmp=tmp+z[i]*v[i]
    for i in range(0,len(z)):
        z[i]=z[i]-v[i]*tmp
    return z

s = np.array([[19/12, 13/12, 5/6, 5/6, 13/12,-17/12], \
    [13/12, 13/12, 5/6, 5/6, -11/12, 13/12], \
    [5/6, 5/6, 5/6, -1/6, 5/6, 5/6], \
    [5/6, 5/6, -1/6, 5/6, 5/6, 5/6], \
    [13/12, -11/12, 5/6, 5/6, 13/12, 13/12], \
    [-17/12, 13/12, 5/6, 5/6, 13/12, 19/12]])
v = np.array([1, 2, 0, 0, 0, 0])
for i in range(100):
    vOld = v.copy()
    z = np.dot(s,v) #wektor nowey
    zMag = math.sqrt(np.dot(z,z)) #norma
    v = z/zMag #nowy wektor
    if np.dot(vOld,v) < 0.0: #prawdzamy czy norma nie zgubila znaku
        sign = -1.0
        v = -v
    else: sign = 1.0
    if math.sqrt(np.dot(vOld - v,vOld - v)) < 1.0e-10: break
lam = sign*zMag
print("Number of iterations =",i)
print("First Eigenvalue =",lam)
print(f"First Vector: {v}")


v2 = np.array([1, 2, 0, 0, 0, 0])
for i in range(100):
    vOld = v2.copy()
    z2 = np.dot(s,v2) #wektor nowey
    z2=ortho(z2,v)
    zMag2 = math.sqrt(np.dot(z2,z2)) #norma
    v2 = z2/zMag2 #nowy wektor
    if np.dot(vOld,v2) < 0.0: #prawdzamy czy norma nie zgubila znaku
        sign = -1.0
        v2 = -v2
    else: sign = 1.0
    if math.sqrt(np.dot(vOld - v2,vOld - v2)) < 1.0e-10: break
lam2 = sign*zMag2
print("Number of iterations =",i)
print("Second Eigenvalue =",lam2)
print(f"Second Vector: {v2}")


