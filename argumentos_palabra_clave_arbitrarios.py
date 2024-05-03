#   Argumentos arbitrarios con palabras clave

#
#       *kwargs
#   Se coloca dos asteriscos (**) antes del parametro

def imprimir_info(**info):
    print(info)     #Lo empaqueta como diccionario
    for clave, valor in info.items():    #Se comporta como diccionario
        print(f'{clave}: {valor}')


imprimir_info(nombre='Adolfo',
              edad='01',
              pais='Perú')