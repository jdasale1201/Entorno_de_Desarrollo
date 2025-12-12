
class espacio:
    def __init__(self, nombre: str, metros_cuadrados: float, ventanas: str):   # ← cambiado: metros_cuadrado:int → metros_cuadrados:float
        self.nombre = nombre
        self.metros_cuadrados = metros_cuadrados   # ← cambiado: atributo renombrado a plural y tipo float
        self.ventanas = ventanas                   # ← mantiene sí/no como texto

    def mostrar_info(self):                        # ← añadido nuevo método mostrar_info()
        return (
            f"Nombre del espacio: {self.nombre}\n"
            f"Metros cuadrados: {self.metros_cuadrados}\n"
            f"Ventanas: {self.ventanas}"
        )

    def __str__(self):                             # ← ajustado para usar mostrar_info()
        return self.mostrar_info()
