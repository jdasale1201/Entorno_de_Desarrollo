class Barco:
    def __init__(self, nombre, posicionX, posicionY, velocidad, rumbo, numeroMunicion):
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.velocidad = max(0, min(velocidad, 20))
        self.rumbo = max(1, min(rumbo, 359))
        self.numeroMunicion = max(0, numeroMunicion)  

    def __str__(self):
        return (f"Barco: {self.nombre}\n"
                f"Posición: ({self.posicionX}, {self.posicionY})\n"
                f"Velocidad: {self.velocidad} km/h\n"
                f"Rumbo: {self.rumbo}°\n"
                f"Munición: {self.numeroMunicion}")

    def disparar(self):
        if self.numeroMunicion > 0:
            self.numeroMunicion -= 1
            print(f"{self.nombre} ha disparado. Munición restante: {self.numeroMunicion}")
        else:
            print(f"{self.nombre} no tiene munición para disparar")

    def setVelocidad(self, nuevaVelocidad):
        self.velocidad = max(0, min(nuevaVelocidad, 20))
        print(f"Velocidad de {self.nombre} actualizada a {self.velocidad} km/h")

    def setRumbo(self, nuevoRumbo):
        self.rumbo = max(1, min(nuevoRumbo, 359))
        print(f"Rumbo de {self.nombre} actualizado a {self.rumbo}°")


barco1 = Barco("Acuático", 10, 20, 15, 90, 5)
barco2 = Barco("Torpedero", 5, 12, 10, 180, 3)
barco3 = Barco("Destructor", 0, 0, 20, 270, 8)

for barco in [barco1, barco2, barco3]:
    print("\nAntes de modificar:")
    print(barco)

    barco.disparar()

    barco.setVelocidad(barco.velocidad + 5)  
    barco.setRumbo((barco.rumbo + 45) % 360)

    print("\nDespués de modificar:")
    print(barco)
    print("-" * 40)
