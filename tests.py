def pideCon():
    '''
    OBJ: pide confirmacion si o no, s o n,
    true o false, t o f, 1 ó 0
    verdadero o falso, verdad o falsedad, v o f,
    ...
    '''
    men=input('Introduce res:') #mensaje    Introduce respuesta
    return men

'''
#PROBADOR
print(pideCon(),'debe ser true')
'''






    














def ent_A_Con(men,dep=False): #entrada a condicion    mensaje
    try:
        encontrada=False
        pos=0
        verds=['si','s',
              'true','t','1', 
              'verdad','verdadero','verdadera'] #verdaderas     ordenadas de mas a menos usadas
        falsas=['no','n',
               'false','f','0',
               'falso','falsa','falsedad']

        men=men.lower() #a minus 
        
        lonVerds=len(verds)
        if (lonVerds==len(falsas)):
            if (dep):
                print('las longs de las listas concuerdan')

            posMax=lonVerds-1 #no te salgas de rango
        
            while not (pos>posMax or encontrada): #*solo si no ha sido encontrada
                if (dep):
                    print('paso:',2*pos+1,', v:',verds[pos])
                    
                if men==verds[pos]:
                    con=True
                    encontrada=True
                
                elif (men==falsas[pos]): #*
                    con=False
                    encontrada=True

                elif (dep):
                    print('paso:',2*pos+2,', f:',falsas[pos])
                           
                pos+=1
                
            if (encontrada):
                if (dep):
                    print('con encontrada')

                return con
                
            else:
                if (dep):
                    print('con NO encontrada')

                raise ValueError
            
        else:
            print('las longs de las listas NO concuerdan')
            raise ValueError
    except:
        print('las longs de las listas NO concuerdan\no con NO encontrada')

'''     
#PROBADOR
#print(ent_A_Con(pideCon(),dep=True))
print(ent_A_Con(pideCon()))
'''




def hayFaltasOrt(con,exp=False): #hay faltas ortograficas     condicion   explicacion
    if (con and exp):
        print('El profesor se lo ha inventado. NO lo ha copiado de sus apuntes corregidos')
    return not con

#'''
#PROBADOR
print(hayFaltasOrt(True),'debe ser False') #si hay faltas ortograficas --> true
print(hayFaltasOrt(False),'debe ser True') #si hay faltas ortograficas --> false
print(hayFaltasOrt(ent_A_Con(pideCon()),exp=True))
#'''






def pregunta(opcs=4): #numero opciones
    letras=['a','b','c','d','e'] #...
    opcsO=opcs #opcs0
    
    while opcs>0:

        print('Hay faltas ortograficas?')
        con=hayFaltasOrt(ent_A_Con(pideCon()))
        print(letras[opcsO-opcs],':',con)

        opcs-=1

'''
#PROBADOR
print(pregunta())
'''

'''
def test(nPregs):
    for pregunta in range(nPregs):
'''


























