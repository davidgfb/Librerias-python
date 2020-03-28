from math import factorial
import cronometro 
#libreria propia adyacente

TIEMPOINICIALPROGRAMA=getTiempoActual()
#funcion propia libreria cronometro

#funcion recursiva
def factorial1(n):
    #PRE: para n entero >-1
    if n==0: return 1
    else: return n*factorial1(n-1)

#PROBADOR
iniciaCronometro() 
print(factorial1(1000))
paraCronometro("propia")

#PROBADOR
iniciaCronometro()
print(factorial(1000))
paraCronometro("nativa")
print ("\nTiempo total del programa:",
       10**6*(getTiempoActual()-TIEMPOINICIALPROGRAMA),"us")

'''
#bucle for
for n in range(1000):
    print(factorial(n))
'''

'''
#bucle while
abierto=True
n=0
while abierto:
    print(factorial(n))
    n+=1
'''

'''
#bucle while1
n=0
while n<1000:
    print(factorial(n))
    n+=1
'''

'''
print(factorial(0),"debe ser 1")
print(factorial(1),"debe ser 1")
print(factorial(2),"debe ser 2")
print(factorial(3),"debe ser 6")
print(factorial(4),"debe ser 24")
print(factorial(5),"debe ser 120")
'''
