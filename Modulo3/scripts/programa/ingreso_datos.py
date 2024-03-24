


def ingreso_entero(msg: str ='Ingrese un número entero: ')->int:
    """Realiza una función recursiva para el ingreso de un número entero"""
    try:
        numero = int(input(msg))
        return numero
    except:
        print('Dato invalido')
        return ingreso_entero(msg)

def ingreso_decimal(msg: str ='Ingrese un número decimal: ')->float:
    """Realiza una función recursiva para el ingreso de un número entero"""
    try:
        numero = float(input(msg))
        return numero
    except:
        print('Dato invalido')
        return ingreso_decimal(msg)


if __name__ == '__main__':
    print(ingreso_entero())