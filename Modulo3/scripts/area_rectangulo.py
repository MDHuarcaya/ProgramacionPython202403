def area_rectangulo(b:float, h: float)-> float:
    """Calcula el área del rectangulo a partir de la base y altura"""
    return b * h

def ingreso_entero(msg='Ingrese un entero positivo'):
    try:
        numero = int(input(msg))
        if numero>0:
            return numero
        print('Numero ingresado es negativo')
        return ingreso_entero(msg)
    except:
        print('Dato ingresado no es un número, vuelva a intentar')
        return ingreso_entero(msg)


# Creen una funcion recursiva, que me permita realizar el ingreso de un número entero positivo
base = ingreso_entero('Ingrese la base: ')
altura = ingreso_entero('Ingrese la altura: ')

area = area_rectangulo(b=base, h=altura)

print(f'El area del rectangulo es {area}')