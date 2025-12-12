
class cliente:
    def __init__(self, nombre:str,DNI:str, telefono:str, alojamiento_actual):
        self.nombre = nombre
        self.DNI = DNI
        self.telefono = telefono
        self.alojamiento_actal = alojamiento_actual

    def __str__(self):
        return(
            f"Nombre: {self.nombre}"
            f"DNI: {self.DNI}"
            f"Telefono: {self.telefono}"
            f"Alojamiento actual: {self.alojamiento_actal}"
        )