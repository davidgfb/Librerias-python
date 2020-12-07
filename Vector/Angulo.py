from ModuloProductoEscalar import productoEscalarDosVectores3D,moduloVector3D
from math import degrees,acos

def anguloEntreDosVectores3D(u,u1,u2,v,v1,v2):
    """6xint-->float
    OBJ: calcula el angulo en grados sexagesimales formado entre
         dos vectores 3D
    PRE: usa productoEscalar,modulo
    """
    productoModulos=moduloVector3D(u,u1,u2)*moduloVector3D(v,v1,v2)

    return degrees(acos(productoEscalarDosVectores3D(u,u1,u2,v,v1,v2)/productoModulos))

"""
#PROBADOR

print(anguloEntreDosVectores3D(0,1,2,3,4,5),"debe ser 27.69456145077678 grados")
print(anguloEntreDosVectores3D(1,2,3,4,5,6),"debe ser 12.933154491899135 grados")
"""
