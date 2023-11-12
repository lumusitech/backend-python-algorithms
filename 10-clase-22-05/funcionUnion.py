#funcion union

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


listaA=[8,6,2,4]
listaB=[10,12,2,4]


def union(listaA,listaB):
    listaNueva=listaA
    for i in listaB:
        if not esta(listaA,i):
            listaNueva.append(i)
    return listaNueva

print(union(listaA,listaB))


