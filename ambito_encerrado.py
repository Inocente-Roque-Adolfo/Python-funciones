#   Ámbito encerrado
#   función dentro de una función (funciones anidadas)

def exterior():
    a = 50  #   a es de ámbito local de exterior

    def interior():
        print(a)    #interior puede acceder a la variable de exterior
    interior()


exterior()
