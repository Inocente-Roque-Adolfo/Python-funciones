#   Multiples declaraciones return

def condicional(value):
    if value > 0:
        return f'{value}: Positivo'
    elif value < 0:
        return f'{value}: Negativo'
    else:
        return f'{value}: Cero'


print(condicional(20))
print(condicional(0))
print(condicional(-20))