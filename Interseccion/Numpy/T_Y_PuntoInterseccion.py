from numpy import array

def t(normal, d, origen, director):
    """3xarray,int-->float
    OBJ: Calcula el parametro t a partir de la normal y
         la d del plano y el origen y vector director del rayo
    PRE: 
    """
    return -(origen@normal+d)/(director@normal)

def pI(t, origen, director):
    """float,2xarray-->array
    OBJ: Calcula el punto de interseccion del plano con el rayo a partir de
         su t, origen y vector director 
    PRE: 
    """
    return array(origen+t*director)

"""
#PROBADOR
#plano
normal=array([2,-3,1])
d=1

#rayo
origen=array([0,1,3])
director=array([1,0,1])

t=t(normal, d, origen, director)
pI=pI(t, origen, director)

print(t,"debe ser -1/3\n", pI,"debe ser [-1/3, 1, 8/3]")
"""
