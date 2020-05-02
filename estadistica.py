#casosTotales #26b+17r+10g+1y
#probabilidadB=26/54=13/27,probR=17/54,probG=10/54,probY=1/54




















































recuentoGlobal=[]
#recuento=[]
caracteresB=[]
caracteresR=[]
caracteresG=[]
caracteresY=[]
recuento=[caracteresB,caracteresR,caracteresG,caracteresY]








































def guarda(caracter):
    '''
    PRE: mensaje=['b','r','g','y']
    '''
    if (caracter=='b')




    
    recuento.append(mensaje)
    print('Valor guardado')

'''
#PROBADOR
print(recuento,'debe ser []')
guarda('a')
print(recuento,"debe ser ['a']")
'''



















def compruebaCValido(caracter):

    cValidos=['b','r','g','y']
    #valido=0
    
    for cValido in cValidos:
        if caracter==cValido:
            guarda(caracter)
            #valido+=1

    #return valido

'''
#PROBADOR
print(compruebaCValido('h'),'debe ser 0')
print(compruebaCValido('b'),'debe ser 1')
'''
























def opuestoR(n):
    return 1-n

'''
#PROBADOR
print(opuestoR(1),'debe ser 0')
print(opuestoR(2),'debe ser -1')
print(opuestoR(0.911),'debe ser 0.09')
'''


































def resetea():
    global recuento
    recuento=[]
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

































def pAcierto(cFav,cPos):
    return cFav/cPos

'''
#PROBADOR
print(pAcierto(1,100),'debe ser 0.01')
print(pAcierto(100,100),'debe ser 1.0')
'''


































def porcentajeF(cFav,cPos):
    return 100*pFracaso(cFav,cPos)

'''
#PROBADOR
print(porcentajeF(1,100),'debe ser 1.8518518518518519')
'''





























def pFracaso(cFav,cPos):
    return 1-pAcierto(cFav,cPos)

'''
#PROBADOR
print(pFracaso(99,100),'debe ser 0.01')
print(pFracaso(1,100),'debe ser 0.99')
'''






























def porcentajeA(cFav,cPos):
    return 100*pAcierto(cFav,cPos)

'''
#PROBADOR
print(porcentajeA(1,100),'debe ser 1.8518518518518519')
'''
















'''
caracteresValidos=[caracteres,valores]
caracteres=['b','r','g','y']
valores=[26,17,10,1]
#caracteresValidos=[['b',26],['r',17],['g',10],['y',1]]
def compruebaNulos():
    for posicion in range(caracteres):
        if caracteres[posicion]==valores[posicion]:
'''            


        
    













'''
def borraCaracteres(caracter):
    for caracter1 in recuento:
        if caracter==caracter1:
'''
    






    
























pY=porcentajeA(1,54)
def muestraRecuentoR():

    #compruebaNulos()

    pB=porcentajeA(26-cuentaCaracteres('b'),54)
    pR=porcentajeA(17-cuentaCaracteres('r'),54)
    pG=porcentajeA(10-cuentaCaracteres('g'),54)
    
    porcentajes=[[pB,'b'],[pR,'r'],[pG,'g'],[pY,'y']] 

    pOrdenados=sorted(porcentajes,reverse=True)

    print('\nrecuento: ',recuento,'\n',

          '\nb(48.15%):',round(pB,2),'%',
          '\nr(31.48%):',round(pR,2),'%',
          '\ng(18.52%):',round(pG,2),'%',
          '\ny(1.85%) :',round(pY,2),'%',

          '\n\nLa decision mas adecuada hasta el momento es:\n',pOrdenados,'\n')

'''
#PROBADOR
guarda('b')
muestraRecuentoR()
print("debe ser recuento:  ['b']  b: 1.8518518518518519 % r: 0.0 % g: 0.0 % y: 0.0 %")
'''

























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


























abierto=True
while abierto:
    mensaje=input('Introduzca caractér o comando: ')
    
    if mensaje=='sal' or mensaje=="cierra": #(1) if 'sal'==mensaje=='cierra':
        #(1) no funciona
        abierto=False
    elif mensaje=='recuento' or mensaje=='vacia':
        muestraRecuentoR()
    elif mensaje=='resetea':
        resetea()
    elif mensaje=="b" or mensaje=="r" or mensaje=="g" or mensaje=="y":
        #(1*) no funciona
        guarda(mensaje)
        muestraRecuentoR()
    else:
        print('Caractér o comando no reconocido.')
     
  


















































