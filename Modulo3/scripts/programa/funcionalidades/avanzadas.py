def calcular_factorial(n:int):
    """Define el factorial recursivo"""
    if n==1 or n==0:
        return 1
    elif n<0:
        raise Exception('El factorial de negativos, no esta definido')
    return n * calcular_factorial(n-1)

def calcular_sumatoria(n:int, p:float)->float:
    """Calcula la sumatoria a la funcion k(n,p)"""
    # Caso base: si n es igual a 1, retornar p
    if n == 1:
        return p
    # Caso recursivo: sumar n*p y llamar recursivamente con n-1
    return n * p + calcular_sumatoria(n - 1, p)