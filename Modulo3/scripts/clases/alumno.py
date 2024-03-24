

class Alumno:
    # constantes
    cursos = list()

    # Inicializador de clase
    def __init__(self, codigo_alumno, nombre, apellido, correo ) -> None:
        
        self.codigo = codigo_alumno
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        pass

    # agregamos un método
    def inscripcion_curso(self):
        curso = input('A que curso desea inscribirse: ')
        self.cursos.append(curso)

        print(f'Se ha inscrito al curso {curso}')
        pass

    pass


# Creo objetos a partir de mi clase
obj1 = Alumno(codigo_alumno='1234', 
              nombre='Camila', 
              apellido='Castillo', 
              correo='camila@gmail.com'
              )

obj2 = Alumno(codigo_alumno='5678', 
              nombre='Erick', 
              apellido='Ferrer', 
              correo='erick@gmail.com'
              )

# Puedo preguntar a cada objeto por sus atributos
print(obj1.nombre)
print(obj2.correo)


# Incribimos al objeto 1 en 2 curso
obj1.inscripcion_curso()
obj1.inscripcion_curso()

print(f'Cursos inscritos para {obj1.nombre}', obj1.cursos)