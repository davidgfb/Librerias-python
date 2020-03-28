from time import time
from math import factorial

def getTiempoActual():
    return time()

TIEMPOINICIALPROGRAMA=getTiempoActual()
tiempoInicialFuncion=TIEMPOINICIALPROGRAMA
#para definir la var tiempoInicialFuncion como double

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
    


#PROBADOR
iniciaCronometro()
paraCronometro("")
print ("\nTiempo total del programa:",
       10**6*(getTiempoActual()-TIEMPOINICIALPROGRAMA),"us")

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
