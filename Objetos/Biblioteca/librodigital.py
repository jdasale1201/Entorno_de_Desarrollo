
# --------------------------
# SUBCLASE: LibroDigital
# Hereda de Libro
# --------------------------
from libro import Libro


class LibroDigital(Libro):
    def __init__(self, titulo, isbn, anno_publicacion, autor,
                contenido, formato, tam_mb, max_descargas):
        super().__init__(titulo, isbn, anno_publicacion, autor, contenido)
        self.formato = formato           # e.g. "PDF", "EPUB"
        self.tam_mb = tam_mb             # tamaño en MB
        self.max_descargas = max_descargas
        self.descargas_realizadas = 0

    def descargar(self):
        """Simula una descarga del libro digital si no se supera el límite."""
        if self.descargas_realizadas < self.max_descargas:
            self.descargas_realizadas += 1
            print(f"Se descarga '{self.titulo}'. Descargas realizadas: {self.descargas_realizadas}")
        else:
            print(f"No se puede descargar '{self.titulo}': se alcanzó el máximo de descargas.")

    def __str__(self):
        base = super().__str__()
        return (
            base + "\n"
            f"  [Digital] Formato: {self.formato}\n"
            f"  Tamaño: {self.tam_mb} MB\n"
            f"  Descargas: {self.descargas_realizadas}/{self.max_descargas}"
        )

