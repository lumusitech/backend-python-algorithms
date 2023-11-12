#funcion MDC maximo divisor comun

def esta(lista,elemento):
    for i in lista:
        if elemento==i:
            return True
    return False

#prueba de esta
listaA=[8,6,2,4]
listaB=[10,12,2,4]
print(esta(listaB,10))


def interseccion(listaA,listaB):
    listaNueva=[]
    for i in listaA:
        if esta(listaB,i):
            listaNueva.append(i)

#prueba interseccion
listaA=[8,6,2,4]
listaB=[10,12,2,4]
print(interseccion(listaA,listaB))


def dameDivisores(numero):
    listaDivisores=[]
    for i in range(1,numero+1):
        if numero%i==0:
            listaDivisores.append(i)
    return listaDivisores

#prueba dameDivisores
listaA=[8,6,2,4]
listaB=[10,12,2,4]
print(dameDivisores(20))




def maximo(listaA):
    maximo=listaA[0] #da un error revisar bien y pensar solucion. si copio a parte esto
                    #funciona bien por lo que tiene un conflicto con algo anterior
    for i in range(1,len(listaA)):
        if listaA[i]>maximo:
            maximo=listaA[i]
    return maximo

#prueba maximo
listaA=[8,6,2,4]
listaB=[10,12,2,4]
print(maximo(listaA))



#uso dameDivisores para crear dos listas, cada una con sus respectivos divisores
listaA=dameDivisores(25)
listaB=dameDivisores(10)
print(listaA,listaB)

def MCD(num1,num2):
    lista1=dameDivisores(num1)
    lista2=dameDivisores(num2)

    lista3=interseccion(lista1,lista2)

    return maximo(lista3)
    #Se puede hacer en una sola linea
    #return (maximo(interseccion(dameDivisores(num1),dameDivisores(num2))))

print(MCD(25,10))

#revisar error con lo que suban en el campus

