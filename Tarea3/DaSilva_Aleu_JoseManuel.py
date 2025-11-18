class Caja:
    def __init__(self, codigo: str, peso_kg: float, descripcion_carga: str, largo: float, ancho: float, altura: float):
        self.codigo = codigo
        self.peso_kg = peso_kg
        self.descripcion_carga = descripcion_carga
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def __str__(self):
        return (f"Caja {self.codigo}: {self.descripcion_carga}, "
                f"Peso: {self.peso_kg} kg, Dimensiones: {self.largo}x{self.ancho}x{self.altura} m")


class Camion:
    def __init__(self, matricula: str, conductor: str, capacidad_kg: float, descripcion_carga: str,
                rumbo: int, velocidad: int):
        self.matricula = matricula
        self.conductor = conductor
        self.capacidad_kg = capacidad_kg
        self.descripcion_carga = descripcion_carga
        self.rumbo = rumbo
        self.velocidad = velocidad
        self.cajas = []

    def peso_total(self) -> float:
        return sum(caja.peso_kg for caja in self.cajas)

    def add_caja(self, caja: Caja):
        if self.peso_total() + caja.peso_kg > self.capacidad_kg:
            raise ValueError(f"No se puede añadir la caja {caja.codigo}: "
                            f"supera la capacidad máxima de {self.capacidad_kg} kg.")
        self.cajas.append(caja)
        print(f"Caja {caja.codigo} añadida correctamente: {caja}")

    def setVelocidad(self, nueva_velocidad: int):
        self.velocidad = nueva_velocidad
        print(f"Nueva velocidad establecida: {self.velocidad} km/h.")

    def setRumbo(self, nuevo_rumbo: int):
        if 1 <= nuevo_rumbo <= 359:
            self.rumbo = nuevo_rumbo
            print(f"Nuevo rumbo establecido: {self.rumbo}°.")
        else:
            raise ValueError("El rumbo debe estar entre 1 y 359 grados.")

    def claxon(self):
        print("Piiiiiiii")

    def __str__(self):
        cajas_info = ""
        for caja in self.cajas:
            cajas_info += str(caja) + "\n"

        return (f"Camión {self.matricula}\n"
                f"Conductor: {self.conductor}\n"
                f"Descripción carga: {self.descripcion_carga}\n"
                f"Capacidad máxima: {self.capacidad_kg} kg\n"
                f"Rumbo: {self.rumbo}°\n"
                f"Velocidad: {self.velocidad} km/h\n"
                f"Número de cajas: {len(self.cajas)}\n"
                f"Peso total actual: {self.peso_total()} kg\n"
                f"Cajas cargadas:\n{cajas_info}")


if __name__ == "__main__":

    camion = Camion("1234-ABC", "Juan Pérez", 5000.0, "Carga general", 90, 80)

    caja1 = Caja("CX001", 1200.5, "Electrodomésticos", 1.2, 0.8, 0.6)
    caja2 = Caja("CX002", 2300.0, "Ropa", 1.0, 1.0, 1.0)
    caja3 = Caja("CX003", 2000.0, "Muebles", 2.0, 1.5, 1.2)

    try:
        camion.add_caja(caja3)
        camion.add_caja(caja1)
        camion.add_caja(caja2)  
    except ValueError as e:
        print("⚠️", e)

    camion.setVelocidad(100)
    camion.setRumbo(270)

    camion.claxon()

    print(camion)
