

# input -> me permite el ingreso de datos por teclado 
#  el tipo de dato que retorna un input es el str


lado = input('Ingrese el valor del lado del cuadrado: ')

lado = int(lado)

area = lado ** 2

# Mostrar los datos
print(lado, type(lado))
print(f'El área del cuadrado de lado {lado} es {area}')
