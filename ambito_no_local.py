#   Ámbito no Local
#   Funcional para funciones anidadas (nonlocal)

def exterior():
    a = 50  # a es de ámbito local de exterior

    def interior():
        nonlocal a
        a = 20
        #print(a)  # interior puede acceder a la variable de exterior

    interior()
    print(a)


exterior()
