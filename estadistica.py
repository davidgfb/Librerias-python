casosTotales=54 #26b+17r+10g+1y
#probabilidadB=26/54=13/27,probR=17/54,probG=10/54,probY=1/54



recuento=[]
def recuento(mensaje):
    '''
    PRE: mensaje=['b','r','g','y']
    '''
    if "b"==mensaje=="r" or "g"==mensaje=="y":
        recuento.append(mensaje)
    else:
        raise ValueError()

'''        
#PROBADOR
abierto=True
while abierto:
    try:
        mensaje=input('Introduzca caractér o comando: ')
        
        if mensaje=='sal' or mensaje=="cierra":
        #if 'sal'==mensaje=='cierra': no funciona
            abierto=False
        elif mensaje=='recuento':
            print(recuento)
        else:
            
                recuento(mensaje)
    except:
        mensaje1=input('Caractér o comando no reconocido. Vuelva a introducirlo: ')
        recuento(mensaje1)
'''    
    



def esNegativo(n):
    '''
    PRE: 0<n<0 
    '''
    negativo=False
    if n<0 or n==-0:
        negativo=True
    else:
        negativo=False
    return negativo

'''
#PROBADOR
print(esNegativo(-0),"debe ser True")
print(esNegativo(0),"debe ser False")
print(esNegativo(+0),"debe ser False")
'''

#override
def vAbs(n):
    if n<0:
        n*=-1
    return n

'''
#PROBADOR
print(vAbs(-1),"debe ser 1")
print(vAbs(0),"debe ser 0")
print(vAbs(1),"debe ser 1")
'''



def factoriza(n):
    '''
    PRE: n>1
    '''
    n=vAbs(n)
    factores=[]
    for i in range(n):
        i+=1
        #print("n%i=",n%i,"i=",i)
        if n%(i)==0 or 1==i==n:
            factores.append(i)
    return factores


#PROBADOR
print(factoriza(13),"debe ser [1,13]")
print(factoriza(26),"debe ser [1,2,13,26]")
print(factoriza(54),"debe ser [1,2,3,6,9,18,27,54]")
print(factoriza(10),"debe ser [1,2,5,10]")
print(factoriza(1),"debe ser [1]")

print(factoriza(-1),"debe ser [-1] + exc")


def esPrimo(n):
    '''
    PRE: n>1
    '''
    primo=False
    if len(factoriza(n))<2:
        primo=True
    else:
        primo=False
    return primo

'''    
#PROBADOR
print(esPrimo(13),"debe ser True")
print(esPrimo(27),"debe ser False")
print(esPrimo(17),"debe ser True")
print(esPrimo(54),"debe ser False")
print(esPrimo(1),"debe ser True")
print(esPrimo(-1),"debe ser True + exc")
'''
#print(esPrimo(-13),"debe ser True + exc")

