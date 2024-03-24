# 1. Librerias
import ingreso_datos
from funcionalidades import maths

from funcionalidades import avanzadas as ad

from funcionalidades.avanzadas import calcular_factorial

# 2. Constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
OPCIONES_MENU = """
¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Función Factorial
    3) Funcion K(n, p)
    4) Salir
"""

# 3. Funciones y/o métodos

def opcion1():
    numero1 = ingreso_datos.ingreso_entero(msg='Ingrese el primero número a sumar: ')
    numero2 = ingreso_datos.ingreso_entero(msg='Ingrese el segundo número a sumar: ')

    resultado = maths.sumar(numero1, numero2)
    print(f'El resultado de la suma {resultado}')

def opcion2():
    n = ingreso_datos.ingreso_entero(msg='Ingrese un número entero positivo: ')
    resultado = ad.calcular_factorial(n)
    print(f'{n}! = {resultado}')

def opcion3():
    n = ingreso_datos.ingreso_entero(msg='Ingrese un número entero positivo: ')
    assert n>0, 'n debe ser un entero positivo'
    p = ingreso_datos.ingreso_decimal(msg='Ingrese un número "p": ')

    resultado = ad.calcular_sumatoria(n=n, p=p)

    print('K(n={n}, p={p})= {resultado}'.format(n=n, p=p, resultado=resultado))

def main():
    print(MENSAJE_BIENVENIDA)
    while True:
        opcion = input(OPCIONES_MENU) # me devuelve un string ''
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion =='4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")

# 4. funcion main
if __name__=='__main__':
    main()