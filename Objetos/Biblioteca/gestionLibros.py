# ================================================
# POO con libros: herencia, composición, agregación
# y asociación. Versión sencilla y didáctica.
# ================================================

from autor import Autor
from biblioteca import Biblioteca
from contenidoLibro import ContenidoLibro
from librodigital import LibroDigital
from librofisico import LibroFisico



# --------------------------
# PROGRAMA DE PRUEBA
# --------------------------
if __name__ == "__main__":
    # Creamos un autor (asociación)
    autor1 = Autor("Isaac Asimov", "Ruso-Estadounidense")

    # Creamos contenidos para los libros (composición)
    contenido_fisico = ContenidoLibro(
        num_paginas=350,
        capitulos=["Prólogo", "Capítulo 1", "Capítulo 2", "Epílogo"]
    )
    contenido_digital = ContenidoLibro(
        num_paginas=220,
        capitulos=["Introducción", "Parte I", "Parte II", "Conclusión"]
    )

    # Creamos libros: físico y digital (herencia)
    libro_fisico = LibroFisico(
        titulo="Fundación",
        isbn="978-1234567890",
        anno_publicacion=1951,
        autor=autor1,
        contenido=contenido_fisico,
        ubicacion="Estantería A3",
        ejemplares_totales=3
    )

    libro_digital = LibroDigital(
        titulo="Yo, Robot",
        isbn="978-0987654321",
        anno_publicacion=1950,
        autor=autor1,
        contenido=contenido_digital,
        formato="EPUB",
        tam_mb=1.8,
        max_descargas=2
    )

    # Creamos una biblioteca (agregación)
    biblioteca = Biblioteca("Biblioteca Central", "Madrid")
    biblioteca.agregar_libro(libro_fisico)
    biblioteca.agregar_libro(libro_digital)

    # Estado inicial
    print("\n=== ESTADO INICIAL ===")
    biblioteca.listar_libros()

    # Usamos algunos métodos que cambian el estado
    print("\n=== OPERACIONES ===")
    libro_fisico.prestar_ejemplar()
    libro_fisico.prestar_ejemplar()
    libro_fisico.devolver_ejemplar()

    libro_digital.descargar()
    libro_digital.descargar()
    libro_digital.descargar()  # aquí ya no debería dejar

    # Estado final
    print("\n=== ESTADO FINAL ===")
    biblioteca.listar_libros()
