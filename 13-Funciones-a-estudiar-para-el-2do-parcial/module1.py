#Funcion: interseccion de elementos de dos conjuntos

def esta(elemento,lista):
    for i in lista:
        if elemento==i:
            return True
    return False

def interseccion(listaA,listaB):
    listaInterseccion=[]
    for i in listaA:
        if esta(i,listaB):
            listaInterseccion.append(i)
    return listaInterseccion

#programa
listaA=[2,3,8,9,12]
listaB=[5,12,9,56,20]

print(interseccion(listaA,listaB))