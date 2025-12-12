# --------------------------
# SUBCLASE: LibroFisico
# Hereda de Libro
# --------------------------
from libro import Libro


class LibroFisico(Libro):
    def __init__(self, titulo, isbn, anno_publicacion, autor,
                contenido, ubicacion, ejemplares_totales):
        super().__init__(titulo, isbn, anno_publicacion, autor, contenido)
        self.ubicacion = ubicacion
        self.ejemplares_totales = ejemplares_totales
        self.ejemplares_disponibles = ejemplares_totales

    def prestar_ejemplar(self):
        """Presta un ejemplar físico si hay disponibles."""
        if self.ejemplares_disponibles > 0:
            self.ejemplares_disponibles -= 1
            print(f"Se presta un ejemplar físico de '{self.titulo}'.")
        else:
            print(f"No quedan ejemplares disponibles de '{self.titulo}'.")

    def devolver_ejemplar(self):
        """Devuelve un ejemplar físico, sin exceder el total."""
        if self.ejemplares_disponibles < self.ejemplares_totales:
            self.ejemplares_disponibles += 1
            print(f"Se devuelve un ejemplar físico de '{self.titulo}'.")
        else:
            print(f"Todos los ejemplares de '{self.titulo}' ya están en la biblioteca.")

    def __str__(self):
        base = super().__str__()
        return (
            base + "\n"
            f"  [Físico] Ubicación: {self.ubicacion}\n"
            f"  Ejemplares: {self.ejemplares_disponibles}/{self.ejemplares_totales}"
        )

