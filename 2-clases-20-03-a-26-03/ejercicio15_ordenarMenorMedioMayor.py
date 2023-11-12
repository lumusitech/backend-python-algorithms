#Ejercicio 15: Indicar menor, medio y mayor

a=5;b=1;c=2

if a<=b and a <=c:
    menor=a
    if b<=c:
        medio=b;mayor=c
    else:
        aux=b;b=c;c=aux
        medio=b;mayor=c
else:
    if b<=a and b<=c:
        aux=a;a=b;b=aux
        menor=a
        if b<=c:
            medio=b;mayor=c
        else:
            aux=b;b=c;c=aux
            medio=b;mayor=c
    else:
        if c<=a and c<=b:
            aux=c;c=a;a=aux
            menor=a
            if c<=b:
                aux=c;c=b;b=aux
                medio=b;mayor=c
            else:
                medio=b;mayor=c
print(menor,medio,mayor)