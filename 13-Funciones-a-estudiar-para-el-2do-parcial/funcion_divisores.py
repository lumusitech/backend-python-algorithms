#Funcion divisores

def divisores(num):
    listaDivisores=[]
    for i in range(1,num+1):
        if not num%i:
            listaDivisores.append(i)
    return listaDivisores

#programa
num=int(input("Ingrese un numero"))
print(divisores(num))