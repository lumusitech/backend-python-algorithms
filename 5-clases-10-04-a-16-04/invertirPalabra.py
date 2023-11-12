#Ejercicio en clases con cadenas 12-04-07
cadn=""
cad=input("Ingrese la palabra a invertir")
for i in cad:
    #cadn=cadn+i aca imprime lo mismo ya que a cadn(cadena vacia)le suma i que recorre la palabra ingresada
    cadn=i+cadn #al poner i adelante en lugar de atras le cambiamos el orden
print(cadn)
