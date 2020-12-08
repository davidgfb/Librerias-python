def t(a,b,c,d, ox,oy,oz, dx,dy,dz): 
    """10xint-->float
    OBJ: Calcula la t del rayo a partir de su origen y
         vector director
    PRE: 
    """
    return -(a*ox+ b*oy+ c*oz+d)/(a*dx+ b*dy+ c*dz)

def pI(t, ox,oy,oz, dx,dy,dz):
    """7xint-->lista
    OBJ: Calcula el punto de interseccion del plano con el rayo
         a partir de su origen y vector director
    PRE:
    """
    return [ox+t*dx, oy+t*dy, oz+t*dz]

"""
#PROBADOR
#plano
#normal
a=2
b=-3
c=1

#punto d altura plano 
d=1

#Rayo
#origen 
ox=0
oy=1
oz=3

#vector director
dx=1
dy=0
dz=1

t=t(a,b,c,d, ox,oy,oz, dx,dy,dz)
pI=pI(t, ox,oy,oz, dx,dy,dz)

print(t,"debe ser -1/3\n", pI,"debe ser [-1/3, 1, 8/3]")
"""    
