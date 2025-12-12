from alojamiento import alojamiento

class casaRural(alojamiento):
    def __init__(self, direccion, ciudad, precio_noche, sala_principal, código, metros_jardin:int, chimenea:str):
        super().__init__(direccion, ciudad, precio_noche, sala_principal, código)
        self.metros_jardin = metros_jardin
        self.chimenea = chimenea

    def __str__(self):
        base = super().__str__()
        return(
            base + "\n"
            f"Metros del jardín: {self.metros_jardin}\n"
            f"Chimenea: {self.chimenea}\n"
        )

