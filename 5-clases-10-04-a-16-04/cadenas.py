#Cadenas

a="hola"
b="chau"

print(a+b)#Con el + se concatenan cadenas
print(b+" "+a)
print(len(a))#Imprime la cantidad de caracteres, no inicia de cero, inicia de uno
print(len("Hola Mundo"))
print("a\nb")#cuenta al salto como un caracter \n
print(len(""))
print(len(" "))
a="mi cadena"
for caracter in a:
    print(caracter)

for caracter in a:
    print(caracter,end="")#pone un caracter al aldo de otro

c="hola como estas"

for letra in c:
    print(letra, end="_")#pongo el separador de cada caracter

