palabra=input("Ingrese una palabra: ")

#intentar resolverlo sin pasar a un array ya que no es necesario, la palabra ya se interpreta por indices
x=palabra[0]
y=palabra[len(palabra)-1]

palabraBase=list(palabra)

palabraBase[0]=y
palabraBase[len(palabra)-1]=x

palabraCambiada="".join(palabraBase)



print(palabraCambiada)




