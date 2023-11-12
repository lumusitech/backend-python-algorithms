palabra=input("Ingrese una palabra")
cont=0

for char in palabra:
    if char=="a" or char=="e"or char=="i"or char=="o"or char=="u":
        cont+=1
print(cont)