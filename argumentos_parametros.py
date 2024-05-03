## Argumentos y parametros
#Parametro: se define dentro de la función
def saludar(parametro):
    mensaje = f'Hola, {parametro} ¡Bienvenido!'
    print(mensaje)


#Argumento: se envia al llamar una función
argumento = 'Adolfo'
saludar(argumento)


#2 parametros
def suma(num1,num2):
    resultado = num1+num2
    print(f'La suma de {num1} y {num2}: {resultado}')


suma(10,5)
