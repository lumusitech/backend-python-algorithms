def maximo(lista):
    maximo=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>maximo:
            maximo=lista[i]
    return maximo

#prrograma
listaA=[8,6,2,48]
print(maximo(listaA))