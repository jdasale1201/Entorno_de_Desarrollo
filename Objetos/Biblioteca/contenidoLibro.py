
# --------------------------
# COMPOSICIÓN: ContenidoLibro
# El contenido forma parte del libro y no tiene
# sentido sin él.
# --------------------------

class ContenidoLibro:
    def __init__(self, num_paginas, capitulos):
        # capitulos será una lista de cadenas
        self.num_paginas = num_paginas
        self.capitulos = capitulos

    def __str__(self):
        return f"{self.num_paginas} páginas, {len(self.capitulos)} capítulos"
