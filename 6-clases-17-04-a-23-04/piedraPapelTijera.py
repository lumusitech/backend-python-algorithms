import random

piedra = 0
papel = 1
tijera = 2

seguirJugando = True
while(seguirJugando):

    print("Piedra Papel Tijera")
    print("Seleccione una opcion valida")
    print("0 ) Piedra\n")
    print("1 ) Papel\n")
    print("2 ) Tijera\n")

    opcion = int(input("Piedra Papel Tijera\n Ingrese Opcion:\n 0 ) Piedra\n 1 ) Papel\n 2 ) Tijera\n"))

    opcionPC = random.randrange(0,3,1)

    if(opcion == piedra):

        if(opcionPC == piedra):
            print("Vos elegiste piedra y yo tambien")
            print("Empatamos")
        else:
            if(opcionPC == papel):
                print("Vos elegiste piedra y yo papel")
                print("Gane yo !!")
            else:
                if(opcionPC == tijera):
                    print("Vos elegiste piedra y yo tijera")
                    print("Ganaste vos !!")
    else:
        if(opcion == papel):
            if(opcionPC == piedra):
                print("Vos elegiste papel y yo piedra")
                print("Ganaste vos !!")
            else:
                if(opcionPC == papel):
                    print("Vos elegiste papel y yo papel")
                    print("Empatamos")
                else:
                    if(opcionPC == tijera):
                        print("Vos elegiste papel y yo tijera")
                        print("Gane yo !!")
        else:# if(opcion == tijera):
            if(opcionPC == piedra):
                print("Vos elegiste tijera y yo piedra")
                print("Gane yo !!")
            else:
                if(opcionPC == papel):
                    print("Vos elegiste tijera y yo papel")
                    print("Ganaste vos !!")
                else:
                    if(opcionPC == tijera):
                        print("Vos elegiste tijera y yo tijera")
                        print("Empatamos")

    print("Presiona 1 para salir y cualquier otra para seguir jugando\n")
    respuesta = int(input("Presiona 1 para salir y cualquier otra para seguir jugando\n"))
    if(respuesta == 1):
        seguirJugando = False

print("Juego Finalizado")




