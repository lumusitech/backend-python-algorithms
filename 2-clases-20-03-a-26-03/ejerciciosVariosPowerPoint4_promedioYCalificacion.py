#Ejercicios varios del powerpoint

n1=int(input("Ingresar primer nota: "))
n2=int(input("Ingresar segunda nota: "))
n3=int(input("Ingresar tercer nota: "))

notaFinal=(n1+n2+n3)/3

if notaFinal>=7:
    print("Ha promocionado")
else:
    if notaFinal>=4 and notaFinal<7:
        print("Debe ir a final")
    else:
        print("Debe recursar")