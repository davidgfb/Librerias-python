from time import sleep
'''"\r" es carriage return abre desde cmd'''
[(print(i,"% [",i*"#",end="]\r"),sleep(1)) for i in range(101)] #list comprehensions, faltan formatting strings "%d" "%s"
