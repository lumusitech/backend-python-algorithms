n=int(input("ingrese un numero"))

for i in range(n): #range(1,n+1) o range(1,n+1,2)
    print("*",end="")

print("\n")

##############################################
#Solucion de la clase
cn=""
muestro="*"
for i in range(n):
    cn=cn+"*" #cn primero vale nada, despues un asterisco y sigue sumando segun lo ingresado
print(cn)