from alojamiento import alojamiento

class apartamento(alojamiento):
    def __init__(self, direccion, ciudad, precio_noche:float, sala_principal:str, código:str, numero_planta: int, ascensor: str):
        super().__init__(direccion, ciudad, precio_noche, sala_principal, código)
        self.numero_planta = numero_planta
        self.ascensor = ascensor

    def __str__(self):
        base = super().__str__()
        return(
            base + "\n"
            f"Planta: {self.numero_planta}"
            f"Ascensor: {self.ascensor}"
        )

