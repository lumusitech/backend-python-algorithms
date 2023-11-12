#Ejercicio de parcial 1: numeros oblongos

def divisores(num):
    listaDivisores=[]
    for i in range(1,num):
        if not num%i:
            listaDivisores.append(i)
    return listaDivisores

num=20
print(divisores(num))