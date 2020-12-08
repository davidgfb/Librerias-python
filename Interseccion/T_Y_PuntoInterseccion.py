from numpy import array

def tArray(normal, d, origen, director):
    return -(origen@normal+d)/(director@normal)

def pI_Array(t, origen, director):
    return array(origen+t*director)

"""
#PROBADOR
#plano
normal=array([2,-3,1])
d=1

#rayo
origen=array([0,1,3])
director=array([1,0,1])

t=tArray(normal, d, origen, director)

print(t,"debe ser -1/3\n", pI_Array(t, origen, director),
      "debe ser [-1/3, 1, 8/3]")
"""

def t(a,b,c,d, ox,oy,oz, dx,dy,dz): #alfa
    """10xint-->float
    OBJ: Calcula la t del rayo a partir de su origen y vector director
    PRE: 
    """
    return -(a*ox+ b*oy+ c*oz+d)/(a*dx+ b*dy+ c*dz)

def pInterseccion(t, ox,oy,oz, dx,dy,dz):
    """7xint-->lista
    OBJ: Calcula el punto de interseccion del plano con el rayo
         a partir de su origen y vector director
    PRE:
    """
    return [ox+t*dx, oy+t*dy, oz+t*dz]

"""
#PROBADOR

#normal
a=2
b=-3
c=1

#plano
d=1

#origen Rayo
ox=0
oy=1
oz=3

#vector director
dx=1
dy=0
dz=1

t=t(a,b,c,d, ox,oy,oz, dx,dy,dz)

print(t,"debe ser -1/3\n", pInterseccion(t, ox,oy,oz, dx,dy,dz),
      "debe ser [-1/3, 1, 8/3]")
"""    
