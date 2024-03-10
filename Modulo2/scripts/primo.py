# Evaluar si un número es primo o no lo es

import math

def evaluar_primo(x):
    """Retornara True si número es primo o False si numero no es primo"""

    es_primo =True
    for i in range(2, x):
        if x%i==0:
            # Uso el break para salir del bucle, dado que se encontro un divisor del número por lo tanto, numero no es primo
            es_primo=False
            break
    return es_primo

# 1. Solicitar un numero al usuario

numero = int(input('Ingrese un número: '))

# Evaluo si número es primo o no
es_primo = evaluar_primo(x=numero)

if es_primo:
    print('El número es primo')
else:
    print('El número no es primo!!')

