#   Documentación de una función

def funcion_basica(num1, num2):
    """
    Realiza operaciones básicas entre dos números.

    :param num1: (int o float) Primer número.
    :param num2: (int o float) Segundo número
    :return: Una tupla con los resultados de las operaciones.
             - suma (int o float): Suma de num1 y num2.
             - resta (int o float): Resta de num1 y num2.
             - multiplicación (int o float): Producto de num1 y num2.
             - division (float): Cociente de num1 dividido por num2 (si num2 no es cero).
    """
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1*num2
    division = num1/num2
    return suma, resta, multiplicacion, division


#   Lo retorna en formato de Tupla
resultados = funcion_basica(64,2)
print(resultados)


#   Docstring de una funcion
def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    :param n: (int) Número entero no negativo.
    :return: (int) El factorial de n.
    :raises RecursionError: Si n es un número negativo.
    """
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


fact = factorial(5)
print(fact)

help(funcion_basica)

print(factorial.__doc__)
