#   Función recursiva
#   Llamado de la función dentro de sí misma
def contar_hasta_cero(n):
    if n<=0:
        print(f'{n} ¡He llegado a cero!')
    else:
        print(n)
        contar_hasta_cero(n-1)

contar_hasta_cero(10)

#   Para evitar una recursividad infinita
#   Se debe poner una condición