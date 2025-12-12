# aviones_agregacion.py
# Ejemplo de agregación:
#   - Un Avion "tiene" una lista de Pasajero,
#     pero los Pasajeros pueden existir de forma independiente.

class Pasajero:
    def __init__(self, dni, nombre, edad, asiento):
        self.dni = dni
        self.nombre = nombre
        self.edad = int(edad)
        self.asiento = asiento

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni}, {self.edad} años, asiento {self.asiento})"


class Avion:
    def __init__(self, matricula, modelo, capacidad, velocidad, rumbo, pasajeros=None):
        if capacidad <= 0:
            raise ValueError("NO ENCESTO AL .")
        
        if (rumbo <= 0 or rumbo >=359.99):
            raise ValueError("El valor del rumbo no es correcto")

        self.matricula = matricula
        self.modelo = modelo
        self.capacidad = int(capacidad)
        self.velocidad = float(velocidad)   # km/h
        self.rumbo = float(rumbo)           # grados

        # Agregación: guardamos una *referencia* a una lista de pasajeros.
        # Si no se pasa ninguna lista, creamos una nueva lista vacía.
        if pasajeros is None:
            self.pasajeros = []
        else:
            self.pasajeros = list(pasajeros)

    def total_pasajeros(self):
        return len(self.pasajeros)

    def add_pasajero(self, pasajero):
        """Intenta añadir un pasajero. Devuelve True si se añade."""
        if self.total_pasajeros() < self.capacidad:
            self.pasajeros.append(pasajero)
            return True
        else:
            print(f"⚠️  No se pudo embarcar a {pasajero.nombre} en {self.matricula}: "
                f"capacidad completa ({self.total_pasajeros()}/{self.capacidad}).")
            return False

    def __str__(self):
        # Si hay pasajeros en la lista, los convertimos a texto uno a uno.
        if self.pasajeros:
            # str(p) llama al __str__ de Pasajero
            lineas_pasajeros = []
            for p in self.pasajeros:
                linea = str(p)
                lineas_pasajeros.append(linea)

            # Unimos todas las líneas con saltos de línea y sangría
            listado = "\n    " + "\n    ".join(lineas_pasajeros)
        else:
            listado = " — sin pasajeros —"

        texto = (
            f"Avión {self.matricula} ({self.modelo})\n"
            f"  Velocidad: {self.velocidad:.0f} km/h   Rumbo: {self.rumbo:.0f}°\n"
            f"  Capacidad: {self.capacidad}  Ocupación: {self.total_pasajeros()}\n"
            f"  Pasajeros:{listado}"
        )
        return texto


def imprimir_estado(titulo, lista_aviones):
    print(f"\n=== {titulo} ===")
    for avion in lista_aviones:
        print(avion)
        print("-" * 60)


if __name__ == "__main__":
    # Creamos algunos pasajeros (existen independientemente de los aviones)
    p1 = Pasajero("11111111A", "Ana López", 28, "12A")
    p2 = Pasajero("22222222B", "Luis Pérez", 35, "12B")
    p3 = Pasajero("33333333C", "María Ruiz", 42, "14C")
    p4 = Pasajero("44444444D", "Javier Gil", 50, "3F")

    # Creamos dos aviones, pasándoles listas de pasajeros (agregación)

    avion1 = Avion("EC-ALB", "A320", capacidad=-3,
                    velocidad=820, rumbo=90,
                    pasajeros=[p1, p2]) 

                
    avion2 = Avion("EC-IES", "B737", capacidad=2,
                    velocidad=780, rumbo=270,
                    pasajeros=[p3])
        
    flota = [avion1, avion2]
        


    # Estado inicial
    imprimir_estado("ESTADO INICIAL", flota)

    # Nuevos pasajeros
    p5 = Pasajero("55555555E", "Carmen Soto", 31, "7A")
    p6 = Pasajero("66666666F", "Pedro Alba", 19, "7B")

    # Intentamos añadirlos a los aviones
    avion1.add_pasajero(p5)   # debería poder entrar
    avion2.add_pasajero(p6)   # puede que no, según capacidad

    # Estado final
    imprimir_estado("DESPUÉS DE AÑADIR PASAJEROS", flota)