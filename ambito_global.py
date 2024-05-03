#Palabra clave global
n = 20
def funcion():
    
    global n
    n = n+20
    print(f'{n}: dentro de la funcion')

funcion()
print(f'{n}: fuera de la funcion')