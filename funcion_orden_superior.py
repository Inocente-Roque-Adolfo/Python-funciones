#   Función de orden superior

def cuadrado(x):
    return x*x


def cubo(x):
    return x**3


def aplicar(funcion, valor):
    return funcion(valor)


#   Referencio
resultado = aplicar(cuadrado,5)
print(resultado)

resultado = aplicar(cubo,5)
print(resultado)


#   Cambio el unico valor por una lista #

def aplicar_funcion_a_lista(funcion,lista):
    rpta = []
    for elemento in lista:
        rpta.append(funcion(elemento))
    return rpta


elevar_lista = [1,2,3,4,5]
#   Almaceno el dato que retorna
salida = aplicar_funcion_a_lista(cubo, elevar_lista)
print(salida)