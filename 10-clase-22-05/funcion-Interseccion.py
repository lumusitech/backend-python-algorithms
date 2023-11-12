#funcion esta que verificca si un elemento esta en una lista

def esta(lista,elemento):
    for i in lista:
        if elemento==i:
            return True
    return False

def interseccion(listaA,listaB):
    listaNueva=[]
    for i in listaA:
        if esta(listaB,i):
            listaNueva.append(i)

##########################################
#otra forma con range
def interseccion(listaA,listaB):
    listaNueva=[]
    for i in range(len(listaA)):
        if esta(listaB,lista[i]):
            listaNueva.append(i)


