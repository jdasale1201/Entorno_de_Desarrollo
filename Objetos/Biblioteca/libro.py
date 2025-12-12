
# --------------------------
# SUPERCLASE: Libro
# --------------------------
class Libro:
    def __init__(self, titulo, isbn, anno_publicacion, autor, contenido):
        self.titulo = titulo
        self.isbn = isbn
        self.anno_publicacion = anno_publicacion

        # Asociación: el libro "conoce" a su autor,
        # pero el autor no es "propiedad" del libro.
        self.autor = autor

        # Composición: el libro "contiene" su contenido.
        self.contenido = contenido

        # Atributos de estado sencillos
        self.disponible = True  # genérico

    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return (
            f"Libro: {self.titulo}\n"
            f"  ISBN: {self.isbn}\n"
            f"  Año publicación: {self.anno_publicacion}\n"
            f"  Autor: {self.autor}\n"
            f"  Contenido: {self.contenido}\n"
            f"  Estado: {estado}"
        )
