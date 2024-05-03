#   Combinación de args y kwargs
def funcion_combinada(*args, **kwargs):
    print('Argumentos posicionales: ',
          args)
    print('Argumentos de palabras clave: ',
          kwargs)

funcion_combinada(1,2,3,4,5,
                  dato1='a',dato2='b',dato3='c')