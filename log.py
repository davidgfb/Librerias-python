'''
def logD(base,n): #n=10^exp
    exponente=

def log(base,n): #n=base^exp
    """
    Obj: Calcula el exponente del log a partir de la base y n
    """
    exponente=n/base
    return exponente

#"""
#PROBADOR
print(log(2,5),'debe ser 2.322')
print(log(5,25),'debe ser 2')
#"""


def log(b,n):
    if n<b:
        return 0  
    return log(n/b,b)+1

#PROBADOR
print(log(2,5),'debe ser 0.4307')




def myLog(x, b):
    
    x: a positive integer
    b: a positive integer; b >= 2
    returns: log_b(x), or, the logarithm of x relative to a base b.
    
    # Tests if x is less than the base, b. If true, then we have found
    # the logarithm of x relative to b
    if x < b:
        # Debug string to see progression, values of x, b
        #print("x < b. " + "x: " + str(x) + " b: " + str(b))
        return 0
    else:
        # Debug string to see progression, values of x, b
        #print("In else. " + "x: " + str(x) + " b: " + str(b))
        return 1 + myLog(x/b, b)

# Examples of calling myLog()
print(myLog(16, 2))
print(myLog(15, 3))








def my_log(x, base):
    count = -1

    while x > 0:
        x /= base
        count += 1
        if x == 0:
            return count


print(my_log(16, 2))

# %timeit %run my_log.py
# 1000 loops, best of 3: 321 us per loop
'''







'''
def logN(n,i): #logE    n es el no      i es el numero de pasos max
    i0=i
    res=0
    while i>0:
        print()
        res+=(((-1)**(i+1))/i)*(n-1)**i#+logN(n,i)

        i-=1
        print('iteraciones rtes:',i,', paso:',i0-i)
        print('el sig calculo sera con logN(',n,',',i,')')
        print()
    return res
        

    
    for i in range(i):  
        if (i>0):
            i+=1 
            res=0

            

            n-=1
            logN(x,n)
            
            if n>0: #si no se ha acabado el no iteraciones
                res=(((-1)**(i+1))/i)*(x-1)**i+logN(x+1,n-1)

            print(,)
        return res
        
#PROBADOR
print(logN(0,10))
'''













def ln(x,i=1000,met=2): #logN   logE
    if met==0:
        res=i*((x**(1/i))-1)
    elif met==1:
        res=i*((x**(i**-1))-1)
    elif met==2:
        res=(i*(x**(i**-1))-i)
    return res

'''
#PROBADOR
import math
e=math.e
print (ln(e),'debe ser',math.log(e))
print (ln(0.5),'debe ser',math.log(0.5))
print (ln(100.0),'debe ser',math.log(100.0))
'''

'''
#TODO
estaria interesante ver un plot con los pasos y la aproximacion para saber cual es
el mejor numero de iteraciones
'''




def log(b,n):
    return ln(n)/ln(b)

#PROBADOR
print(log(5,2),'debe ser 0.431')






























