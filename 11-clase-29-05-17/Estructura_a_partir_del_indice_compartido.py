#Ejercicio dado 29-05-17 sobre correspondencia de indice, parecido al ejercicio 6
#de la practica de listas. Estudiar para el parcial, listas que se corresponden por el indice

def esta(n,lista):
    for i in range(len(lista)):
        if lista[i]==n:
            return i
    return -1 #Para indicar que no esta el registro

#


#Programa

dni=[11,12,13,14,15]
ape=["Maria Gomez","Felipe PeÃ±a","Agustina Soros","Teresa Rodriguez","no reg"]
localidad=["CABA","San Luis","Misiones","Santa Cruz","Corrientes","null"]
NumDni=int(input("Ingresar DNI"))
saberSiEsta=esta(NumDni,dni)#Se asigna a una variable el resultado de la funcion

#Se pregunta que retorno
if saberSiEsta!=-1:
    print("El apellido correspondiente es ",ape[saberSiEsta]," y vive en ",localidad[saberSiEsta])
else:
    print ("ese DNI No esta en la lista")