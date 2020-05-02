









#ascii=[asciiDecimal,alfabeto]




def decimalA_Ascii(entero):
    '''
    A-Z 65-90
    a-z 97-122
    '''
    alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
              'R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
              'r','s','t','u','v','w','x','y','z']
    try:
        if entero<91:
            formato=65 #minuscula
        else:
            formato=71 #mayuscula
        return alfabeto[entero-formato]

    except:
        return("Entero fuera del rango alfabeto")

'''
#PROBADOR
print(decimalA_Ascii(0))
print(decimalA_Ascii(65),'debe ser A mayuscula')
print(decimalA_Ascii(90),'debe ser Z mayuscula')
print(decimalA_Ascii(97),'debe ser a minuscula')
print(decimalA_Ascii(122),'debe ser z minuscula')
'''

















def esMul(entero,multiplo):
    #ademas es divisible por 2 o multiplo de 2
    if (entero%multiplo==0):
        multiplo=True
    else:
        multiplo=False
    return multiplo


'''
#PROBADOR
print(esMul(0,2),'debe ser True')
print(esMul(1,2),'debe ser False')
print(esMul(2,2),'debe ser True')
print(esMul(3,2),'debe ser False')
'''






















def rellenaCeros(binario,longitudBits):
    mensajeBinario=str(binario)
    cerosFaltantes=longitudBits-len(mensajeBinario)
    if cerosFaltantes>0:
        relleno=cerosFaltantes*'0'+mensajeBinario
    else:
        relleno=binario
    return relleno
    
'''
#PROBADOR
print(rellenaCeros(000,8),'debe ser 00000000')
print(rellenaCeros(100,8),'debe ser 00000100')
'''




















def cambiaBit(bit):
    if bit==0:
        bit=1
    else:
        bit=0
    return bit

'''
#PROBADOR
print(cambiaBit(0),'debe ser 1')
print(cambiaBit(1),'debe ser 0')
'''




















'''
def imprimeNumsBins(longitudBits):
    #por multiplos
    numerosDecimal=0

    unidades=1 
    decenas=1
    centenas=0
    millar=0

    decMillar=0
    centMillar=0
    millon=0
    decMillon=1
    
    while numerosDecimal<2**longitudBits:
        unidades=cambiaBit(unidades) #posicion 0: '0 es par'
        if esMultiplo(numerosDecimal,256):
            decMillon=cambiaBit(decMillon)
        elif esMultiplo(numerosDecimal,128):
            millon=cambiaBit(millon)
        elif esMultiplo(numerosDecimal,64):
            centMillar=cambiaBit(centMillar)
        elif esMultiplo(numerosDecimal,32):
            decMillar=cambiaBit(decMillar)
        elif esMultiplo(numerosDecimal,16):
            millar=cambiaBit(millar)
        elif esMultiplo(numerosDecimal,8):
            centenas=cambiaBit(centenas)
        elif esMultiplo(numerosDecimal,4):
            decenas=cambiaBit(decenas)
       
            
        resultado=str(decMillon)+str(millon)+str(centMillar)+str(decMillar)+str(millar)+str(centenas)+str(decenas)+str(unidades)
        print('numsDecimal:',numerosDecimal,rellenaCeros(resultado,8))
        numerosDecimal+=1
'''        
        
    


'''
#PROBADOR
imprimeNumsBins(8)
'''
















#@override
def rango(numero,saltos=1,inclusive=False,informatico=True):
    if informatico:
        contador=0
    else:
        contador=1
    resultado=[]
    if inclusive:
        while contador<=numero:
            if esMul(contador,saltos):
                resultado.append(contador)
            contador+=1
    else:
        while contador<numero:
            if esMul(contador,saltos):
                resultado.append(contador)
            contador+=1
    return resultado

'''
#PROBADOR
print(rango(10),'debe ser [0,1,2,3,4,5,6,7,8,9]') #decimal
print(rango(2),'debe ser [0,1]') #binario
print(rango(10,inclusive=True),'debe ser [0,1,2,3,4,5,6,7,8,9,10]')
print(rango(10,saltos=10,inclusive=True),'debe ser [0,10]')
print(rango(10,inclusive=1,informatico=False),'debe ser [1,2,3,4,5,6,7,8,9,10]')

tupla=[]
for numero in range(10):
    tupla.append(numero)
print(tupla,'debe ser',rango(10))
'''






















def mod(numero,modulo=10):
    return numero%modulo

'''
#PROBADOR
print(mod(0),'debe ser 0')
print(mod(10),'debe ser 0')
print(mod(10,2),'debe ser 0')
print(mod(11,2),'debe ser 1')
'''

def modulo(numero,modulo=10):
    #polimorfismo
    return mod(numero,modulo)

'''
#PROBADOR
print(modulo(0),'debe ser 0')
print(modulo(10),'debe ser 0')
print(modulo(10,2),'debe ser 0')
print(modulo(11,2),'debe ser 1')
'''
























def vectorA_Cadena(vector):
    cadena=''
    for elemento in vector:
        cadena+=str(elemento)
    return cadena

'''
#PROBADOR
print(vectorA_Cadena(['r','o','m','a']),'debe ser roma')
'''
















def leeCadenaReves(cadena):
    cadenaDerecho=[]
    for letra in cadena:
        cadenaDerecho.append(letra)
    return vectorA_Cadena(cadenaDerecho[::-1])

'''
#PROBADOR
print(leeCadenaReves('roma'),'debe ser amor')
'''

































#vector=['a']
def reseteaVector():
    global vector
    vector=[]

'''
#PROBADOR
reseteaVector()
print(vector,'debe ser []')
'''




vector=[]
def cadenaA_Vector(cadena):
    global vector
    vector.append(cadena)

#reseteaCadena(cadena)

'''
#PROBADOR
cadenaA_Vector('11111111')
print(vector,"debe ser ['11111111']")
reseteaVector()
print(vector,'debe ser []')
'''


















def limpiaVectorEnteros(vector):
    vectorLimpio=[]
    for elemento in vector:
        vectorLimpio.append(int(elemento))
    return vectorLimpio

'''
#PROBADOR
print(limpiaVectorEnteros(['1',0]),'debe ser [1,0]')
'''


def limpiaVectorCadena(vector):
    vectorLimpio=[]
    for elemento in vector:
        vectorLimpio.append(str(elemento))
    return vectorLimpio

'''
#PROBADOR
print(limpiaVectorCadena([1,'a']),"debe ser ['1','a']")
'''







'''
def vectorA_Matriz(vector,filas=1,columnas=len(vector)):
    if (filas and columnas):
        matriz=[filas][columnas]
    else:
        matriz=vector
    #for elemento in vector:
        
    return matriz
'''

'''
#PROBADOR
print(vectorA_Matriz(['(0,0)','(0,1)']))
print(vectorA_Matriz(['(0,0)','(0,1)'],2,1))
'''

















def enteroA_Bin(numero,implementacion=1):
    binario=['00000000', '00000001', '00000010', '00000011', '00000100', '00000101',
             '00000110', '00000111', '00001000', '00001001', '00001010', '00001011',
             '00001100', '00001101', '00001110', '00001111', '00010000', '00010001',
             '00010010', '00010011', '00010100', '00010101', '00010110', '00010111',
             '00011000', '00011001', '00011010', '00011011', '00011100', '00011101',
             '00011110', '00011111', '00100000', '00100001', '00100010', '00100011',
             '00100100', '00100101', '00100110', '00100111', '00101000', '00101001',
             '00101010', '00101011', '00101100', '00101101', '00101110', '00101111',
             '00110000', '00110001', '00110010', '00110011', '00110100', '00110101',
             '00110110', '00110111', '00111000', '00111001', '00111010', '00111011',
             '00111100', '00111101', '00111110', '00111111', '01000000', '01000001',
             '01000010', '01000011', '01000100', '01000101', '01000110', '01000111',
             '01001000', '01001001', '01001010', '01001011', '01001100', '01001101',
             '01001110', '01001111', '01010000', '01010001', '01010010', '01010011',
             '01010100', '01010101', '01010110', '01010111', '01011000', '01011001',
             '01011010', '01011011', '01011100', '01011101', '01011110', '01011111',
             '01100000', '01100001', '01100010', '01100011', '01100100', '01100101',
             '01100110', '01100111', '01101000', '01101001', '01101010', '01101011',
             '01101100', '01101101', '01101110', '01101111', '01110000', '01110001',
             '01110010', '01110011', '01110100', '01110101', '01110110', '01110111',
             '01111000', '01111001', '01111010', '01111011', '01111100', '01111101',
             '01111110', '01111111', '10000000', '10000001', '10000010', '10000011',
             '10000100', '10000101', '10000110', '10000111', '10001000', '10001001',
             '10001010', '10001011', '10001100', '10001101', '10001110', '10001111',
             '10010000', '10010001', '10010010', '10010011', '10010100', '10010101',
             '10010110', '10010111', '10011000', '10011001', '10011010', '10011011',
             '10011100', '10011101', '10011110', '10011111', '10100000', '10100001',
             '10100010', '10100011', '10100100', '10100101', '10100110', '10100111',
             '10101000', '10101001', '10101010', '10101011', '10101100', '10101101',
             '10101110', '10101111', '10110000', '10110001', '10110010', '10110011',
             '10110100', '10110101', '10110110', '10110111', '10111000', '10111001',
             '10111010', '10111011', '10111100', '10111101', '10111110', '10111111',
             '11000000', '11000001', '11000010', '11000011', '11000100', '11000101',
             '11000110', '11000111', '11001000', '11001001', '11001010', '11001011',
             '11001100', '11001101', '11001110', '11001111', '11010000', '11010001',
             '11010010', '11010011', '11010100', '11010101', '11010110', '11010111',
             '11011000', '11011001', '11011010', '11011011', '11011100', '11011101',
             '11011110', '11011111', '11100000', '11100001', '11100010', '11100011',
             '11100100', '11100101', '11100110', '11100111', '11101000', '11101001',
             '11101010', '11101011', '11101100', '11101101', '11101110', '11101111',
             '11110000', '11110001', '11110010', '11110011', '11110100', '11110101',
             '11110110', '11110111', '11111000', '11111001', '11111010', '11111011',
             '11111100', '11111101', '11111110', '11111111']
    if implementacion:

        resultado=''
        if numero==0:
            resultado='0'
        else:
            while numero>0:
                resultado+=str(numero%2)
                numero//=2
        resultado=int(leeCadenaReves(resultado))
    else:
        resultado=[]
        if numero==0:
            resultado=0
        else:
            while numero>0:
                resultado.append(numero%2)
                numero//=2
            resultado=vectorA_Cadena(resultado[::-1])
    return resultado

'''
#PROBADOR
print(enteroA_Bin(0),'debe ser 0')
print(enteroA_Bin(10),'debe ser 1010')

print(enteroA_Bin(0,0),'debe ser 0')
print(enteroA_Bin(10,0),'debe ser 1010')
'''

'''
#imprime los primeros 256 numeros binarios
vector=[]
lonBits=8
nMax=2**lonBits
for numero in rango(nMax):
    #print(rellenaCeros(enteroA_Bin(numero),8))
    vector.append(rellenaCeros(enteroA_Bin(numero),8))
print(vector)
'''























































'''
def imprimeBinario(longBits):
    ultimoN=2**longBits
    print('ultimoN:',ultimoN)
    print('rango:',rango(ultimoN,10))
    for numero in rango(ultimoN,10):
        print(numero)

'''

'''
#PROBADOR
imprimeBinario(8)
'''
































def decimalABin(entero):
    #max 8 bits = 1 byte
    binario=[]








def textoA_Array(alfabeto):
    posicion=0
    print("[",end="")
    for letra in alfabeto:
        posicion+=1
        if (posicion<len(alfabeto)):
            print("'",letra,"',",sep="",end="")
        else:
            print("'",letra,"']",sep="",end="")
        

'''
#PROBADOR
textoA_Array('abc')
print(" debe ser ['a','b','c']")
'''








