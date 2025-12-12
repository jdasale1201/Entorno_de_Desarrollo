from alojamiento import alojamiento
from casaRural import casaRural
from apartamento import apartamento
from Espacio import espacio
from cliente import cliente

class agencia:
    def __init__(self, nombre: str, correo_contacto:str):
        self.nombre = nombre
        self.correo_contacto = correo_contacto
        self.alojamientos = []

    def agregar_alojamiento(self, casa):
        self.alojamientos.append(casa)
        print(f"Se agrega '{alojamiento}' a la agencia '{self.nombre}'.")

    def contarAlojamientos(self):
        print("Los alojamientos que tenemos son:")
        for casa in self.alojamientos:
            print(casa)

    def __str__(self):
        return(
            f"Nombre: {self.nombre}"
            f"Contacto: {self.correo_contacto}"
        )

if __name__ == "__main__":
    
    alojamiento1 = alojamiento("Calle Rafael Alberti", "Cádiz", 120.75, "Salón", "ABC-123")

    apartamento1 = apartamento("Calle Rodrigo", "San Fernando", 145.54, "Cocina", "ZYX-987", 2, "No")

    CasaRural1 = casaRural("Benitez", "Chiclana", 234.04, "Comedor", "ABC-456", 43, "Si")

    cliente1 = cliente("Jose Manuel Da Silva Aleu", "123456789A", "098765432", {alojamiento1})