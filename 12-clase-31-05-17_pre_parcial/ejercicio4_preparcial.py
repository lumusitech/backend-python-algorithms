#Ejercicio 4 pre parcial - correspondencia por indices

LisCli=["AlvarezC","AlvarezW","Bieira","Datola","Flamingo","Irusta"]
LisSaldo=[-50,0,-150000,-30000,45000,-1500]
LisTel=[1520004000,1570701111,1580801010,154444,1577779999,1533334545]

def BuscaIndice(cadena,lista):
    for i in range(len(lista)):
        if cadena==lista[i]:
            return i

    return -1

apellido="Bieira"
j=BuscaIndice(apellido,LisCli)

if j==-1:
    print("El cliente no se encuentra en la lista")
else:
    if LisSaldo[j]>=0:
        print("Sin deuda")
    else:
        if LisSaldo[j]>=-2000:
            print("Descubierto pautado")
        else:
            if LisSaldo[j]<-2000:
                print("Debe regularizar su deuda, Saldo ",LisSaldo[j],", Telefono: ",LisTel[j])



