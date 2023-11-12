#3er ejercicio pre parcial

def Cubo(n):
    return n**3


def SumaCubos(a,b,c):
    return Cubo(a)+Cubo(b)+Cubo(c)


def Cubos(n):
    #para separar cada cifra se puede dividir(resto) %10
    c=n%10
    b=n//10%10
    a=n//10//10%10
    if SumaCubos(a,b,c)==n:
        return True
    else:
        return False

#Programa
for i in range(100,1000):
    if Cubos(i):
        print(i)



