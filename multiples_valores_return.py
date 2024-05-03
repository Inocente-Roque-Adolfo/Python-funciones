#   Retornar más de un valor en un return

def funcion_basica(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1*num2
    division = num1/num2
    return suma, resta, multiplicacion, division


#   Lo retorna en formato de Tupla
resultados = funcion_basica(64,2)
print(resultados)