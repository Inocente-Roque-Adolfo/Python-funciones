#   Paso por valor
def modificar_valor(x):
    x = (x + 10)
    print(f'Dentro de la función: {x}')


numero = 5
modificar_valor(numero)
print(f'Fuera de la función: {numero}')


#   Paso por referencia
#   Si se referencia los objetos mutables si modifican su valor
def modificar_lista(lista):
    lista.append(4)
    print(f'Dentro de la función: {lista}')

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(f'Fuera de la función: {mi_lista}')

