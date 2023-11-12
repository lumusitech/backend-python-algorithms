#Ejercicio 9: Uso de or en las guardas

dni1=30612453
dni2=23763290
dni3=21448503
dni4=34582048
dni5=15364857

dni=int(input("Ingrese un DNI: "))
if dni==dni1 or dni==dni2 or dni==dni3 or dni==dni4 or dni==dni5:
    print("El DNI ingresado Ya se encuentra en nuestra lista.")
else:
    print("El DNI ingresado no se encuentra en nuestra lista.")