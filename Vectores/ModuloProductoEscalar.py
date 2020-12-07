from math import sqrt

def moduloVector3D(v,v1,v2):
    """3xint-->int
    OBJ: calcula el modulo de un vector 3D
    PRE:
    """
    return sqrt(v**2+v1**2+v2**2)

"""
#PROBADOR

print(moduloVector3D(0,1,2),"debe ser 2.23606797749979")
print(moduloVector3D(1,2,3),"debe ser 3.7416573867739413")
"""

def productoEscalarDosVectores3D(u,u1,u2,v,v1,v2):
    """6xint-->int
    OBJ: calcula el producto escalar de dos vectores 3D
    PRE: 
    """
    return u*v+u1*v1+u2*v2

"""
#PROBADOR

print(productoEscalarDosVectores3D(0,1,2,3,4,5),"debe ser 14")
print(productoEscalarDosVectores3D(1,2,3,4,5,6),"debe ser 32")
"""


