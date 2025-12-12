
class espacio:
    def __init__(self, nombre:str, metros_cuadrado:int, ventanas:str):
        self.nombre = nombre
        self.metros_cuadrado = metros_cuadrado
        self.ventanas = ventanas

    def __str__(self):
        return(
            f"Metros cuadrados: {self.metros_cuadrado}"
            f"Ventanas: {self.ventanas}"
        )