import tkinter as tk
from tkinter import simpledialog
from math import cos, sin, radians
import random
import winsound  # Solo en Windows, para un pitido simple al disparar

# Clase Barco
class Barco:
    def __init__(self, nombre, x, y, velocidad, rumbo, municion, color="red"):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.velocidad = max(0, min(velocidad, 20))
        self.rumbo = max(1, min(rumbo, 359))
        self.municion = max(0, municion)
        self.color = color
        self.icon = None

    def disparar(self):
        if self.municion > 0:
            self.municion -= 1
            print(f"{self.nombre} ha disparado. Munición restante: {self.municion}")
            try:
                winsound.Beep(1000, 150)  # Pitido al disparar
            except:
                pass  # Si no está en Windows, se ignora
        else:
            print(f"{self.nombre} no tiene munición para disparar")

    def setVelocidad(self, v):
        self.velocidad = max(0, min(v, 20))

    def setRumbo(self, r):
        self.rumbo = max(1, min(r, 359))

    def setMunicion(self, m):
        self.municion = max(0, m)

    def mover(self):
        self.x += self.velocidad * cos(radians(self.rumbo)) * 0.1
        self.y -= self.velocidad * sin(radians(self.rumbo)) * 0.1

# Interfaz gráfica
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Barcos")

        self.barcos = []
        self.barco_activo = None

        self.canvas = tk.Canvas(root, width=600, height=400, bg="lightblue")
        self.canvas.pack()

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Button(control_frame, text="Crear Barco", command=self.crear_barco).grid(row=0, column=0)
        self.selector = tk.StringVar()
        self.selector_menu = tk.OptionMenu(control_frame, self.selector, ())
        self.selector_menu.grid(row=0, column=1)

        tk.Button(control_frame, text="Disparar", command=self.disparar_barco).grid(row=0, column=2)
        tk.Button(control_frame, text="Aumentar Velocidad", command=lambda: self.modificar_velocidad(1)).grid(row=1, column=0)
        tk.Button(control_frame, text="Disminuir Velocidad", command=lambda: self.modificar_velocidad(-1)).grid(row=1, column=1)
        tk.Button(control_frame, text="Rumbo +45°", command=lambda: self.modificar_rumbo(45)).grid(row=1, column=2)
        tk.Button(control_frame, text="Rumbo -45°", command=lambda: self.modificar_rumbo(-45)).grid(row=1, column=3)
        tk.Button(control_frame, text="Añadir Munición", command=lambda: self.modificar_municion(1)).grid(row=2, column=0)
        tk.Button(control_frame, text="Quitar Munición", command=lambda: self.modificar_municion(-1)).grid(row=2, column=1)

        self.barco_size = 20

        # Crear los 3 barcos iniciales con colores fijos
        colores_iniciales = ["red", "blue", "green"]
        nombres_iniciales = ["Acuático", "Torpedero", "Destructor"]
        posiciones = [(50, 50), (100, 100), (150, 150)]
        velocidades = [15, 10, 20]
        rumbos = [90, 180, 270]
        municiones = [5, 3, 8]

        for i in range(3):
            b = Barco(nombres_iniciales[i], posiciones[i][0], posiciones[i][1],
                      velocidades[i], rumbos[i], municiones[i], colores_iniciales[i])
            self.barcos.append(b)

        self.actualizar_selector()
        self.actualizar_canvas()

    def crear_barco(self):
        nombre = simpledialog.askstring("Nombre", "Nombre del barco:")
        x = simpledialog.askfloat("Posición X", "Posición X:")
        y = simpledialog.askfloat("Posición Y", "Posición Y:")
        velocidad = simpledialog.askfloat("Velocidad", "Velocidad (0-20):")
        rumbo = simpledialog.askfloat("Rumbo", "Rumbo (1-359):")
        municion = simpledialog.askint("Munición", "Número de munición:")
        # Color aleatorio
        color = "#" + "".join(random.choices("0123456789ABCDEF", k=6))
        barco = Barco(nombre, x, y, velocidad, rumbo, municion, color)
        self.barcos.append(barco)
        self.actualizar_selector()

    def actualizar_selector(self):
        menu = self.selector_menu["menu"]
        menu.delete(0, "end")
        for b in self.barcos:
            menu.add_command(label=b.nombre, command=lambda nombre=b.nombre: self.seleccionar_barco(nombre))
        if self.barcos:
            self.seleccionar_barco(self.barcos[-1].nombre)

    def seleccionar_barco(self, nombre):
        for b in self.barcos:
            if b.nombre == nombre:
                self.barco_activo = b
                self.selector.set(nombre)
                break

    def disparar_barco(self):
        if self.barco_activo:
            self.barco_activo.disparar()

    def modificar_velocidad(self, cambio):
        if self.barco_activo:
            self.barco_activo.setVelocidad(self.barco_activo.velocidad + cambio)

    def modificar_rumbo(self, cambio):
        if self.barco_activo:
            nuevo_rumbo = (self.barco_activo.rumbo + cambio) % 360
            if nuevo_rumbo == 0: nuevo_rumbo = 1
            self.barco_activo.setRumbo(nuevo_rumbo)

    def modificar_municion(self, cambio):
        if self.barco_activo:
            self.barco_activo.setMunicion(self.barco_activo.municion + cambio)

    def actualizar_canvas(self):
        self.canvas.delete("all")
        for b in self.barcos:
            b.mover()
            # Crear un icono de barco de color
            img = tk.PhotoImage(width=self.barco_size, height=self.barco_size)
            img.put((b.color,), to=(0, 0, self.barco_size, self.barco_size))
            self.canvas.create_image(b.x, b.y, image=img)
            # Guardar referencia para que no se borre
            b.icon = img
            # Dibujar nombre
            self.canvas.create_text(b.x, b.y - 10, text=b.nombre, fill="black")
        self.root.after(100, self.actualizar_canvas)

# Ejecutar la app
root = tk.Tk()
app = App(root)
root.mainloop()
