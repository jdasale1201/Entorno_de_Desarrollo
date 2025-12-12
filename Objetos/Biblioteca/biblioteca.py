
# --------------------------
# AGREGACIÓN: Biblioteca
# Una biblioteca "agrupa" libros, pero los libros
# pueden existir fuera de ella.
# --------------------------
class Biblioteca:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.libros = []  # lista de libros (agregación)

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se agrega '{libro.titulo}' a la biblioteca '{self.nombre}'.")

    def listar_libros(self):
        print(f"\nBiblioteca: {self.nombre} ({self.ciudad})")
        print("Libros en catálogo:")
        if not self.libros:
            print("  [Sin libros]")
        for libro in self.libros:
            print("--------------------------------------------------")
            print(libro)

    def __str__(self):
        return f"Biblioteca '{self.nombre}' en {self.ciudad} con {len(self.libros)} libros."

