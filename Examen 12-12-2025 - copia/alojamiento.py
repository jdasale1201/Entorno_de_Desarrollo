class alojamiento:
    def __init__(self, direccion: str, ciudad:str, precio_noche:float, sala_principal:str, código:str):

        self.direccion = direccion
        self.ciudad = ciudad
        self.precio_noche = precio_noche
        self.sala_principal = sala_principal
        self.código = código

    def __str__(self):
        return(
            f"Dirección: {self.direccion}\n"
            f"Ciudad: {self.ciudad}\n"
            f"Precio por noche: {self.precio_noche}\n"
            f"Sala principal: {self.sala_principal}\n"
            f"Código: {self.código}\n"
        )

