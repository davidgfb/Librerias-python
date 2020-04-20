casosTotales=54 #26b+17r+10g+1y
#probabilidadB=26/54=13/27,probR=17/54,probG=10/54,probY=1/54






recuentoGlobal=[]
recuentoVacio=[]
recuento=[]
def guarda(mensaje):
    '''
    PRE: mensaje=['b','r','g','y']
    '''
    recuento.append(mensaje)
    print('Valor guardado')

'''
#PROBADOR
print(recuento,'debe ser []')
guarda('a')
print(recuento,"debe ser ['a']")
'''



def resetea():
    global recuento
    recuento=recuentoVacio
    print('Recuento reseteado')

'''
#PROBADOR
guarda('a')
print(recuento,"debe ser ['a']")
resetea()
print(recuento,'debe ser []')
'''


def cuentaCaracteres(mensaje):
    caracteres=0
    for caracter in recuento:
        if caracter==mensaje:
            caracteres+=1
    return caracteres

'''
#PROBADOR
guarda('b')
print(cuentaCaracteres('b'),'debe ser 1')
'''

def porcentaje(mensaje):
    return 100*mensaje/54

'''
#PROBADOR
print(porcentaje(1),'debe ser 1.8518518518518519')
'''


def muestraRecuento():
    print('recuento: ',recuento,' b:',porcentaje(cuentaCaracteres('b')),'%',
          'r:',porcentaje(cuentaCaracteres('r')),'%',
          'g:',porcentaje(cuentaCaracteres('g')),'%',
          'y:',porcentaje(cuentaCaracteres('y')),'%')

'''
#PROBADOR
guarda('b')
muestraRecuento()
print("debe ser recuento:  ['b']  b: 1.8518518518518519 % r: 0.0 % g: 0.0 % y: 0.0 %")
'''



abierto=True
while abierto:
    mensaje=input('Introduzca caractér o comando: ')
    
    if mensaje=='sal' or mensaje=="cierra": #(1) if 'sal'==mensaje=='cierra':
        #(1) no funciona
        abierto=False
    elif mensaje=='recuento':
        muestraRecuento()
    elif mensaje=='resetea':
        resetea()
    elif mensaje=="b" or mensaje=="r" or mensaje=="g" or mensaje=="y":
        #(1*) no funciona
        guarda(mensaje)
    else:
        print('Caractér o comando no reconocido.')
     
  










def esNegativo(n):
    '''
    PRE: 0>n>0 
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

'''
#PROBADOR
print(factoriza(13),"debe ser [1,13]")
print(factoriza(26),"debe ser [1,2,13,26]")
print(factoriza(54),"debe ser [1,2,3,6,9,18,27,54]")
print(factoriza(10),"debe ser [1,2,5,10]")
print(factoriza(1),"debe ser [1]")

print(factoriza(-1),"debe ser [-1] + exc")
'''

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

