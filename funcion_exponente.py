"""
#Si no se entrega el argumento de exponente se considera por defecto 2
"""


def elevar(base, e=1):
    rpta = base ** e
    print(rpta)


elevar(3)
elevar(3,2)

print('')


def exponente(num_base, exp=2):
    num_result = 1
    for i in range(exp):
        num_result = num_base * num_result
    print(num_result)


exponente(2,
          1)
exponente(2)
exponente(2,
          3)
exponente(2,
          4)
