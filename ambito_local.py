#   Solo se usa la variable en la función
def function():
    x = 10  #   x es de ambito local
    print(x)


function()

#   Variable de ámbito local
y = 20


def funcion():
    y = 30
    print(y,' esta en la función')


funcion()
print(y,' esta fuera de la función')
