#Argumentos posicionales
#Se respeta el orden de los argumentos dependiendo de los parametros
def nombre_completo(nombre, apellido):
    cadena = f'{nombre} {apellido}'
    print(cadena)


nombre_completo("Adolfo",
                "IR")
nombre_completo("IR",
                "Adolfo")
