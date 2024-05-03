#   Retornar variables para usar su valor
def suma(a,
         b):
    resultado = a+b
    return resultado
    print('Este mensaje no se muestra termino en return')


#   Para usar lo retornado se debe almacenar el valor en una nueva variable
rpta = suma(5,6)
print(rpta)
print(suma(5,6))


