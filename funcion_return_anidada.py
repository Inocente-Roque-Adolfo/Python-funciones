def multiplicador(factor):
    def funcion_interna(numero):
        return numero * factor
    return funcion_interna


multiplicar_por_10 =  multiplicador(10)
print(multiplicar_por_10(3))

multiplicar_por_5 =  multiplicador(5)
print(multiplicar_por_5(5))


