hucha=0
banco=0
lineasArchivo=[]
caracteresEnteros=[]

def devuelveDinTotal(hucha=0,banco=0):
    return str(hucha+banco)+' euros'

'''
#PROBADOR
print(devuelveDinTotal(10,100),'debe ser 110 euros')
print(devuelveDinTotal(),'debe ser 0 euros')
'''


def leeArchivo(nombre='ahorrosG.py'):
    archivo = open(nombre, 'r')
    for linea in archivo.readlines():
        lineasArchivo.append(linea)
    print(lineasArchivo)
    archivo.close()




def guardaArchivo(nombre='ahorrosG.py',hucha=0,banco=0):
    archivo = open(nombre, 'w')
    cadena='hucha='+str(hucha)+'\nbanco='+str(banco)
    archivo.write(cadena)
    archivo.close()





































def cargaVarsArchivo(nombre='ahorros.py'):
    for linea in lineasArchivo:
        for caracter in linea:
            for entero in range(10):
                #print(entero)
                if caracter==entero:
                    caracteresEnteros.append(caracter)
                    #print('encontre un entero')
        print(caracter)
    print(caracteresEnteros)
                
'''
#PROBADOR
guardaArchivo()
leeArchivo()
print('debe ser:\nhucha=0\nbanco=0')
cargaVarsArchivo()
'''























            
    
