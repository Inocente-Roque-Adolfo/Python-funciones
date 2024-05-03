#Argumentos con palabra clave
#No se conoce el orden de los parametros
def saludos(nombre, saludo):
    mensaje = f'{saludo}, {nombre}'
    print(mensaje)

#indicar a que parametro corresponde
saludos(saludo="Hola",
        nombre="Adolfo")

saludos("Adolfo",
        "Hola")
