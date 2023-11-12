"""Ejercicio 4 - Practica 5: funcion que compara dos lista y devuelve la mas
corta, si son iguales devuelve la primera"""
listaA=[0,5,6,4,3,8]
listaB=[1,9,6,4,5]
def laMasCorta(listaA,listaB):
    if len(listaA)==len(listaB):
        return listaA
    else:
        if len(listaA)<len(listaB):
            return listaA
        else:
            return listaB

#programa
print(laMasCorta(listaA,listaB))
