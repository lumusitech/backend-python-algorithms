import random
apellido=input("Ingrese un apellido")
clave=""
for char in apellido:
    if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
        clave=clave+char
while len(clave) < 4:
    clave=clave+"*"
clave=clave+ str(random.randrange(10))
print("La clave generada es ",clave," del apellido ",apellido)