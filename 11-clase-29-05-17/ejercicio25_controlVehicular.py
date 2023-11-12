#Ejercicio 25 de la practica 5 - listas:
def controlVehicular(ruta):
    if ruta!="ruta8":
        return -1 #el -1 como valor que representa que no pertenece a ruta8.
                  #podria haber usado otra valor para que lo considere mas adelante
    for patente in darPatente(ruta):
        if controlVelocidad(patente)>100:
            if reincidente(patente):
                enviarMulta(patente,costoActual()*2)#por dos porque es reincidente
            else:
                enviarMulta(patente,costoActual())#En este caso no es reincidente por lo que no se *2

