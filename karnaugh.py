#from criptografia import rango,rellenaCeros,enteroA_Bin

entsBin=['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', 1000,
        1001, 1010, 1011, 1100, 1101, 1110, 1111]

a=0
b=0
c=0
d=0
letras=[a,b,c,d]


'''
#imprime los primeros 16 numeros binarios
vector=[]
lonBits=4
nMax=2**lonBits
for numero in rango(nMax):
    #print(rellenaCeros(enteroA_Bin(numero),8))
    vector.append(rellenaCeros(enteroA_Bin(numero),4))
print(vector)
'''


for entBin in entsBin:
    for pos in range(4):
        
        letras[pos]==entBin[pos]
        print('entBin:',entBin,'pos:',pos,'letra:',letras[pos],'entBin[pos]:',
              entBin[pos])
        
