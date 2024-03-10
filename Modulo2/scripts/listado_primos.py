# Brindar un listado de los número primos del 1 al 100


def evaluar_primo(x):
    """Retornara True si número es primo o False si numero no es primo"""

    es_primo =True
    for i in range(2, x):
        if x%i==0:
            # Uso el break para salir del bucle, dado que se encontro un divisor del número por lo tanto, numero no es primo
            es_primo=False
            break
    return es_primo

# Lo que voy a evaluar es los número del 1 al 100
listado_primos = []
for i in range(1, 101):
    # evaluaré cada número
    es_primo = evaluar_primo(i)

    if es_primo:
        listado_primos.append(i)

print(listado_primos)



