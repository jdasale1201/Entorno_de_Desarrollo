from alojamiento import alojamiento
from casaRural import casaRural
from apartamento import apartamento
from Espacio import espacio
from cliente import cliente

class agencia:   # ← cambiado: nombre de clase en PascalCase
    def __init__(self, nombre: str, correo_contacto: str):
        self.nombre = nombre
        self.correo_contacto = correo_contacto
        self.alojamientos = []   # mantiene lista de alojamientos

    def agregar_alojamiento(self, alojamiento):   # ← cambiado: parámetro ahora se llama alojamiento
        self.alojamientos.append(alojamiento)
        print(f"Se agrega '{alojamiento}' a la agencia '{self.nombre}'.")

    def quitar_alojamiento(self, codigo):         # ← añadido nuevo método quitar_alojamiento()
        for a in self.alojamientos:
            if a.codigo == codigo:                # ← usa atributo codigo del alojamiento
                self.alojamientos.remove(a)
                print(f"Alojamiento con código {codigo} eliminado de la agencia '{self.nombre}'.")
                return
        print(f"No se encontró alojamiento con código {codigo} en la agencia '{self.nombre}'.")

    def mostrar_info(self):                       # ← añadido nuevo método mostrar_info()
        print(f"Agencia: {self.nombre}")
        print(f"Correo de contacto: {self.correo_contacto}")
        print("Alojamientos gestionados:")
        for a in self.alojamientos:
            print(a)                              # ← imprime cada alojamiento usando su __str__

    def contar_alojamientos(self):                # ← cambiado: ahora devuelve número en lugar de imprimir
        return len(self.alojamientos)

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"            # ← añadido salto de línea
            f"Contacto: {self.correo_contacto}"
        )


if __name__ == "__main__":

    
    alojamiento1 = alojamiento("Calle Rafael Alberti", "Cádiz", 120.75, "Salón", "ABC-123")
    apartamento1 = apartamento("Calle Rodrigo", "San Fernando", 145.54, "Cocina", "ZYX-987", 2, "No")
    casa_rural1 = casaRural("Benitez", "Chiclana", 234.04, "Comedor", "ABC-456", 43, "Si")
    cliente1 = cliente("Jose Manuel Da Silva Aleu", "123456789A", "098765432", alojamiento1)
    
    print("=== Alojamiento ===")
    print(alojamiento1, "\n")

    print("=== Apartamento ===")
    print(apartamento1, "\n")

    print("=== Casa Rural ===")
    print(casa_rural1, "\n")

    print("=== Cliente ===")
    print(cliente1, "\n")
