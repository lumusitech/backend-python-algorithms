#funcion diferencia

def esta(lista,elemento):
    for i in lista:
        if elemento==i:
            return True
    return False

listaA=[8,6,2,4]
listaB=[10,12,2,4]

def diferencia(listaA,listaB):
    listaNueva=[]
    for i in listaA:
        if not esta(listaB,i):
            listaNueva.append(i)
    return listaNueva

print(diferencia(listaA,listaB))