class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)

class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)


p = Pelicula("El Padrino", duracion=175, lanzamiento=1972)
p2 = Pelicula("Avatar", duracion=200, lanzamiento=2008)
catalogo_netflix = Catalogo([p])  # Añado una lista con una película desde el principio
catalogo_amazon = Catalogo([p2])

# mostrando el catalogo de peliculas actual
catalogo_netflix.mostrar()
catalogo_amazon.mostrar()

catalogo_netflix.agregar(Pelicula(titulo='Rapidos y furiosos 9', duracion=150, lanzamiento=2019))
catalogo_netflix.mostrar()