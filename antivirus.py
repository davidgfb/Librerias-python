

def devuelveHashMd5(archivo):
    #md5,sha256,sha512,sha3
    hash='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    #en hexadecimal
    return hash

'''
#PROBADOR
print(devuelveHashMd5('virus.exe')
      =='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
      'debe ser True')
'''

def aislaArchivo(archivo):
    print('Archivo puesto en cuarentena')

'''
#PROBADOR
aislaArchivo('virus.exe')
'''


def comparaHashes(hashArchivo):
    listaNegra='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    numeroCoincidencias=0
    
    for hashMaligno in listaNegra:
        if hashArchivo==hashMaligno:
            aislaArchivo(archivo)
            numeroCoincidencias=1
        else:
            numeroCoincidencias=0
        return numeroVirus


        


def escaneaDirectorio(directorio): # *.*
    directorio='virus.exe','1.txt' 
    
    numeroVirus=0

    if range(directorio)>1:
        for archivo in directorio:
            print('Escaneando archivo: ',archivo)
            for hashMaligno in listaNegra:
                if hash(archivo)==hashMaligno:
                    aislaArchivo(archivo)
                    numeroVirus+=1
    else:
        for hashMaligno in listaNegra:
                if hash(archivo)==hashMaligno:
                    aislaArchivo(archivo)
                    numeroVirus+=1
    print('Directorio escaneado. Se encontraron: ',numeroVirus,' archivos infectados')

#PROBADOR
escaneaDirectorio('c:')


        
