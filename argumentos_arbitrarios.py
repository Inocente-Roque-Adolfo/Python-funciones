#   Argumentos posicionales arbitrarios

#
#       *args
#   Se coloca un asterisco (*) antes del parametro
def sum_numeros(*numeros):
    print(numeros)  #empaqueta los argumentos en una tupla
    resultados = sum(numeros)
    print(resultados)


sum_numeros(1,
            2,
            3,
            4,
            5,
            6,
            7)
