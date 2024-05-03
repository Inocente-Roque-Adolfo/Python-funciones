#   Factorial de un número
#   5!  5*4*3*2*1

def factorial(n):
    """

    :param n:
    :return:
    """
    if n ==0 or n==1:
        return 1
    else:
        print(n)
        return n * factorial(n-1)


fact = factorial(5)
print(fact)
