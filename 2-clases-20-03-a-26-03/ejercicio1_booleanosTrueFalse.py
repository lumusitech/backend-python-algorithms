#Practica 2 - Ejrcicio 1: Booleanos True y False

a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))
print("Usted ingresÃƒÂ³ los valores:", a, b, c)
print(a, "es mayor que", b, 7==7) #true
print(a, "y", b, "son iguales", 54<55) #true
print(a, "es el mayor de todos", 23<=23+1) #true
print(b, "es el menor de todos", 20-5!=20+5) #true
print(a, "es mayor que alguno de los otros dos", 20/2!=10) #false
print(a, "es menor o igual que alguno de los otros dos", 2-1!=2 and 2-1!=1) #false
print("Los tres numeros son iguales", 5<=(2-1)**2 or 5>=6) #false
print("Los tres numeros son distintos", 6**3==25*5 and 7=="7") #false
print(a, "es par", 3<4 and 5<6) #true
print("alguno es par", 25**2==(23+2)**2) #true
print("ninguno es par", 1 and True) #true
print("todos son pares", 0 == False or 0==True) #true
print(a, "es multiplo de 3", 3-1!=2) #false
print(a, "es multiplo de 3 y de 5", False>True) #false
print(a, "es multiplo de 3 y par", 3**2==9 and 2*0>False) #false
print(a, "-", b, "da un numero positivo", 5<5-1 or 3!=3) #false
print(a, "-", b, "da un numero par positivo", ( 6/5 )**4 / ( 6/5 )**2==(6/5)**2) #true

