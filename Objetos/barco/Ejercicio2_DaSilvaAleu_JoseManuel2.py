import tkinter as tk

# Funciones de la lógica original
def convertir():
    try:
        a = float(entry_input.get())
        resultado = (a * (9/5)) + 32
        mostrar_resultado(f"{a}°C son {resultado}°F")
    except ValueError:
        mostrar_resultado("Introduce un número válido")

def tabla_multiplicar():
    try:
        a = int(entry_input.get())
        resultado = "\n".join([f"{i} x {a} = {i*a}" for i in range(1, 11)])
        mostrar_resultado(resultado)
    except ValueError:
        mostrar_resultado("Introduce un número entero válido")

def salir():
    root.destroy()

def mostrar_resultado(texto):
    resultado_label.config(text=texto)

# Funciones de control de ventana
def minimizar():
    root.iconify()

def maximizar_restaurar():
    global maximizado
    if maximizado:
        root.geometry(ventana_original)
        boton_maximizar.config(text="□")
    else:
        root.state('zoomed')
        boton_maximizar.config(text="❐")
    maximizado = not maximizado

# Configuración de la ventana
root = tk.Tk()
root.title("Menú Interactivo")
root.configure(bg="#D8BFD8")
root.geometry("800x400")
ventana_original = "800x400"
maximizado = False

# Marco principal con borde negro
marco = tk.Frame(root, bg="black", bd=2)
marco.pack(expand=True, fill="both", padx=5, pady=5)

# Frame de control de ventana
frame_control = tk.Frame(marco, bg="#D8BFD8")
frame_control.pack(fill="x", side="top", pady=5)

boton_cerrar = tk.Button(frame_control, text="X", command=salir, bg="red", fg="white", width=4)
boton_cerrar.pack(side="right", padx=2)

boton_maximizar = tk.Button(frame_control, text="□", command=maximizar_restaurar, bg="grey", fg="white", width=4)
boton_maximizar.pack(side="right", padx=2)

boton_minimizar = tk.Button(frame_control, text="_", command=minimizar, bg="grey", fg="white", width=4)
boton_minimizar.pack(side="right", padx=2)

# Frame principal para botones e input
frame_izquierda = tk.Frame(marco, bg="#D8BFD8")
frame_izquierda.pack(side="left", expand=True, fill="both", padx=20, pady=20)

# Input para el número
entry_input = tk.Entry(frame_izquierda, font=("Arial", 14))
entry_input.pack(fill="x", pady=10)

# Botones principales
boton1 = tk.Button(frame_izquierda, text="Conversión de temperatura", command=convertir,
                   bg="#FF7F7F", fg="black", font=("Arial", 14))
boton1.pack(fill="x", pady=5)

boton2 = tk.Button(frame_izquierda, text="Tabla de multiplicar", command=tabla_multiplicar,
                   bg="#ADD8E6", fg="purple", font=("Arial", 14))
boton2.pack(fill="x", pady=5)

boton3 = tk.Button(frame_izquierda, text="Salir", command=salir,
                   bg="#90EE90", fg="white", font=("Arial", 14))
boton3.pack(fill="x", pady=5)

# Frame derecho para resultados
frame_derecha = tk.Frame(marco, bg="#E6E6FA", bd=2, relief="sunken")
frame_derecha.pack(side="right", fill="both", expand=True, padx=20, pady=20)

resultado_label = tk.Label(frame_derecha, text="Aquí aparecerán los resultados", bg="#E6E6FA",
                           font=("Arial", 14), justify="left")
resultado_label.place(relx=0.05, rely=0.4, anchor="w")  # Altura media

root.mainloop()
