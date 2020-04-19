from time import time
from math import factorial







def factorialIterativo(n):
    factorial=1
    for i in range(n):
        i+=1
        factorial*=i
    return factorial

#PROBADOR
print(factorialIterativo(13),'debe ser 6227020800')















def getTiempoActual():
    return time()

tiempoInicialFuncion=getTiempoActual()
#para definir la var tiempoInicialFuncion como double
TIEMPOINICIALPROGRAMA=getTiempoActual()

def setTiempoInicialFuncion(valor):
    tiempoInicialFuncion=valor
    #modifica var global tiempoInicialFuncion
    
def getTiempoInicial():
    return tiempoInicialFuncion
    #consulta valor var global tiempoInicialFuncion

def iniciaCronometro():
    setTiempoInicialFuncion(getTiempoActual())
    
def paraCronometro(mensaje):
    print("\nFunción",mensaje,"terminada en",
          10**6*(getTiempoActual()-getTiempoInicial()),"us")
    
#funcion recursiva
def factorial1(n):
    #PRE: para n entero >-1
    if n==0: return 1
    else: return n*factorial1(n-1)

'''
#PROBADOR
iniciaCronometro()
print(factorial1(1000),"debe ser ")
paraCronometro("propia")
'''

'''
#PROBADOR
iniciaCronometro()
print(factorial(1000),"debe ser ")
paraCronometro("nativa")
print ("\nTiempo total del programa:",
       10**6*(getTiempoActual()-TIEMPOINICIALPROGRAMA),"us")
'''

'''
minuto = 60s
hora = 3600s
dia = 86400s
semana = 604800s
mes = 2592000s (30*dias) o 2419200s (4*semanas, 28*dias)  
año = 31104000s
decada = 311040000s
'''

'''
(m)mili 1000* o 10**3*
(u)micro 10**6*
(n)nano 10**9* (billion = mil millones NO billon = 10**10)
'''

'''
#bucle for
for n in range(1000):
    print(factorial1(n)) 
'''

'''
#bucle while
abierto=True
n=0
while abierto:
    print(factorial1(n))
    n+=1
'''

'''
#bucle while1
n=0
while n<1000:
    print(factorial1(n))
    n+=1
'''

'''
print(factorial1(0),"debe ser 1")
print(factorial1(1),"debe ser 1")
print(factorial1(2),"debe ser 2")
print(factorial1(3),"debe ser 6")
print(factorial1(4),"debe ser 24")
'''
