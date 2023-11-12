def esta(lista,elemento):
    for i in lista:
        if elemento==i:
            return True
    return False

def dameDivisores(numero):
    listaDivisores=[]
    for i in range(1,numero+1):
        if numero%i==0:
            listaDivisores.append(i)
    return listaDivisores



def oblongo(n,lista):
    if not n:
        return True
    else:

        for i in range(len(lista)):
            if esta(lista,lista[i]+1):
                if lista[i]*(lista[i]+1)==n:
                    return True
        return False

#Programa
num=int(input("Ingrese un numero"))
resultado=oblongo(num,dameDivisores(num))
print(dameDivisores(num))
print(resultado)