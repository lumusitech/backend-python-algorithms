#eercicio24 - centrar una palabra

cadena=input("ingrese una palabra")

for i in range(int((80/2)-(len(cadena)/2))):
    print(" ",end="")
print(cadena)

##############################################################################
#solucion de clase
#Estudiar de esta forma

cn="" #es importante inicializar afuera para saber de donde se parte

for i in range(40-len(cadena)//2):
    cn=cn+" "
print(cn,end="")
print(cadena)

#########################################################################
#otra solucion

a=len(cadena)
cd="-"
es=""
mi=a/2
c=40-mi
for i in range(1,80+1):
    if(i==c):
        es=es+cadena
    else:
        es=es+cd
print(es)