#Funcion esta elemento en lista

def esta(elemento,lista):
    for i in lista:
        if elemento==i:
            return True
    return False

#Programa
num=int(input("Ingrese un numero:"))
lista=[0,5,6,8,12,5,7]
print(esta(num,lista))