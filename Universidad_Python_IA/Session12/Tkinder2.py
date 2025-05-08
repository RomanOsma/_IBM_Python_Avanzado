"""
Guía de estudio de Tkinter en Python:
--------------------------------------
Este módulo presenta ejemplos prácticos organizados de componentes básicos de Tkinter,
incluyendo Labels, Buttons, Entry, Text, y Checkbuttons.

Cada ejemplo se activa desde un menú principal para que el estudiante
pueda practicar de forma ordenada y sin saturar la pantalla.

Incluye:
- Ejemplos prácticos y variados.
- Comparaciones y buenas prácticas.
- Ejercicios propuestos con soluciones.

Autor: Tu nombre
Fecha: Abril 2025
"""

import tkinter as tk
from tkinter import messagebox

# ========================
# Funciones de Ejemplos
# ========================

def ejemplo_labels():
    """
    Muestra una ventana con ejemplos de Labels usando 'pack'.
    Cada Label es un texto con diferentes colores.
    """
    ventana = tk.Toplevel()
    ventana.title("Ejemplo: Labels")

    frame = tk.Frame(ventana)
    frame.pack(pady=10)

    lbl1 = tk.Label(frame, text="Etiqueta Pack 1", fg="blue")
    lbl1.pack(pady=5)

    lbl2 = tk.Label(frame, text="Etiqueta Pack 2", fg="green")
    lbl2.pack(pady=5)

    # Ejemplo adicional: Label multilinea
    lbl3 = tk.Label(frame, text="Etiqueta\ncon múltiples\nlíneas", fg="red", justify="center")
    lbl3.pack(pady=5)

def ejemplo_buttons():
    """
    Muestra una ventana con Buttons usando 'grid' para organizar en una cuadrícula.
    """
    ventana = tk.Toplevel()
    ventana.title("Ejemplo: Buttons")

    frame = tk.Frame(ventana)
    frame.pack(pady=10)

    btn1 = tk.Button(frame, text="Botón 1", command=lambda: messagebox.showinfo("Acción", "Botón 1 presionado"))
    btn1.grid(row=0, column=0, padx=5, pady=5)

    btn2 = tk.Button(frame, text="Botón 2", command=lambda: messagebox.showinfo("Acción", "Botón 2 presionado"))
    btn2.grid(row=0, column=1, padx=5, pady=5)

    # Alternativa: Usar 'pack' en lugar de 'grid'
    # Aunque 'pack' es más sencillo, 'grid' da mejor control para varios botones.

def ejemplo_entry():
    """
    Muestra una ventana con un campo Entry para introducir texto,
    y un botón que muestra el texto ingresado.
    """
    ventana = tk.Toplevel()
    ventana.title("Ejemplo: Entry")

    frame = tk.Frame(ventana)
    frame.pack(pady=10)

    entry = tk.Entry(frame, width=30)
    entry.grid(row=0, column=0, padx=5)

    btn = tk.Button(frame, text="Mostrar texto",
                    command=lambda: messagebox.showinfo("Texto ingresado", f"Has escrito: {entry.get()}"))
    btn.grid(row=0, column=1, padx=5)

def ejemplo_text():
    """
    Muestra una ventana con un widget Text para ingresar múltiples líneas de texto.
    """
    ventana = tk.Toplevel()
    ventana.title("Ejemplo: Text")

    frame = tk.Frame(ventana)
    frame.pack(pady=10)

    text = tk.Text(frame, height=5, width=40)
    text.pack()

    # Ejemplo adicional: Botón para obtener el contenido
    def mostrar_contenido():
        contenido = text.get("1.0", tk.END)  # '1.0' significa línea 1, carácter 0
        messagebox.showinfo("Contenido del Text", contenido.strip())

    btn = tk.Button(frame, text="Mostrar contenido", command=mostrar_contenido)
    btn.pack(pady=5)

def ejemplo_checkbuttons():
    """
    Muestra una ventana con Checkbuttons (checkboxes).
    Permite seleccionar múltiples opciones.
    """
    ventana = tk.Toplevel()
    ventana.title("Ejemplo: Checkbuttons")

    frame = tk.Frame(ventana)
    frame.pack(pady=10)

    var1 = tk.IntVar()
    var2 = tk.IntVar()

    chk1 = tk.Checkbutton(frame, text="Opción 1", variable=var1)
    chk2 = tk.Checkbutton(frame, text="Opción 2", variable=var2)

    chk1.pack()
    chk2.pack()

    def mostrar_seleccion():
        seleccion = f"Opción 1: {'Sí' if var1.get() else 'No'}, Opción 2: {'Sí' if var2.get() else 'No'}"
        messagebox.showinfo("Selección", seleccion)

    btn = tk.Button(frame, text="Confirmar selección", command=mostrar_seleccion)
    btn.pack(pady=5)

# ========================
# Comparaciones de Técnicas
# ========================

# Pack vs Grid
# - Pack es más simple y rápido, ideal para pocas opciones.
# - Grid ofrece un control total sobre la ubicación de los elementos en filas y columnas, lo cual es ideal para diseños más complejos.

# Lambda vs Funciones Normales
# - Lambda es útil para acciones rápidas y cortas, como las asignadas a botones.
# - Las funciones normales son mejores para procesos complejos que requieren mayor reutilización.

# ========================
# Ejercicios Prácticos Guiados
# ========================

def label_dinamico():
    """
    Cambia el texto de un Label al presionar un botón.
    """
    ventana = tk.Toplevel()
    ventana.title("Label Dinámico")

    label = tk.Label(ventana, text="Texto inicial")
    label.pack(pady=10)

    def cambiar_texto():
        label.config(text="Texto cambiado")

    boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
    boton.pack(pady=10)

def contador_clicks():
    """
    Muestra un contador de clics.
    Cada vez que presionas un botón, se incrementa el contador.
    """
    ventana = tk.Toplevel()
    ventana.title("Contador de Clics")

    contador = 0
    label = tk.Label(ventana, text=f"Has presionado el botón: {contador} veces")
    label.pack(pady=10)

    def incrementar_contador():
        nonlocal contador
        contador += 1
        label.config(text=f"Has presionado el botón: {contador} veces")

    boton = tk.Button(ventana, text="Contar", command=incrementar_contador)
    boton.pack(pady=10)

def entrada_validada():
    """
    Valida si el texto ingresado en un Entry es un número.
    """
    ventana = tk.Toplevel()
    ventana.title("Entrada Validada")

    entry = tk.Entry(ventana, width=30)
    entry.pack(pady=10)

    def verificar_entrada():
        texto = entry.get()
        if texto.isdigit():
            messagebox.showinfo("Validación", "El texto es un número.")
        else:
            messagebox.showerror("Error", "El texto no es un número.")

    boton = tk.Button(ventana, text="Verificar", command=verificar_entrada)
    boton.pack(pady=10)

def seleccion_multiple():
    """
    Muestra un ejemplo de selección múltiple usando Checkbuttons.
    """
    ventana = tk.Toplevel()
    ventana.title("Selección Múltiple")

    frame = tk.Frame(ventana)
    frame.pack(pady=10)

    var1 = tk.IntVar()
    var2 = tk.IntVar()

    chk1 = tk.Checkbutton(frame, text="Opción 1", variable=var1)
    chk2 = tk.Checkbutton(frame, text="Opción 2", variable=var2)

    chk1.pack()
    chk2.pack()

    def mostrar_seleccion():
        seleccion = f"Opción 1: {'Sí' if var1.get() else 'No'}, Opción 2: {'Sí' if var2.get() else 'No'}"
        messagebox.showinfo("Selección", seleccion)

    btn = tk.Button(frame, text="Confirmar selección", command=mostrar_seleccion)
    btn.pack(pady=5)

# ========================
# Menú Principal
# ========================

def main():
    """
    Crea la ventana principal donde se seleccionan los ejemplos a ejecutar.
    """
    root = tk.Tk()
    root.title("Menú de Ejemplos de Tkinter")

    # Título del menú
    tk.Label(root, text="Seleccione un ejemplo para mostrar:", font=("Arial", 14)).pack(pady=10)

    # Botones del menú que llaman a las funciones de ejemplo
    ejemplos = [
        ("Ejemplo de Labels", ejemplo_labels),
        ("Ejemplo de Botones", ejemplo_buttons),
        ("Ejemplo de Entry", ejemplo_entry),
        ("Ejemplo de Text", ejemplo_text),
        ("Ejemplo de Checkbuttons", ejemplo_checkbuttons),
        ("Label Dinámico", label_dinamico),
        ("Contador de Clics", contador_clicks),
        ("Entrada Validada", entrada_validada),
        ("Selección Múltiple", seleccion_multiple),
    ]

    for texto, funcion in ejemplos:
        tk.Button(root, text=texto, width=30, command=funcion).pack(pady=5)

    # Botón para salir
    tk.Button(root, text="Salir", width=30, command=root.quit).pack(pady=20)

    root.mainloop()

# ========================
# Ejecución del Programa
# ========================

if __name__ == "__main__":
    main()
