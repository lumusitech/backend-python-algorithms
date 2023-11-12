#Ejercicio 24, trabajado 29-05-17, de la practica 5 - Lista:
#Funcion que devuelve el costo del auxilio mecanico
# ya secuenta con varias funciones supuestamente ya definidas por lo que solo se llama en este ejercicio
def pagara(cliente,localidad):
    costo=0
    usados=0
    if(cobertura(cliente))=="oro" and radioCobertura(cliente,localidad):
        return costo# o puedo escribir pass y no hace nada
    else: #A esto se le llama escalonador por su forma de estructura
        if(cobertura(cliente))=="oro" and not radioCobertura(cliente,localidad):
            costo=30
        else:
            if(cobertura(cliente))=="plata" and radioCobertura(cliente,localidad) and usados(cliente)<5:
                costo=0
                usados=usados+1#acumulador
            else:
                if(cobertura(cliente))=="plata" and not radioCobertura(cliente,localidad) and usados(cliente)<5:
                    costo=30
                    usados=usados+1
                else:
                    if(cobertura(cliente))=="plata" and not radioCobertura(cliente,localidad) and usados(cliente)>5:
                        costo=50+30
                        usados=usados+1
                    else:
                        if(cobertura(cliente))=="plata" and radioCobertura(cliente,localidad) and usados(cliente)>5:
                            costo=50
                            usados=usados+1

    return costo








