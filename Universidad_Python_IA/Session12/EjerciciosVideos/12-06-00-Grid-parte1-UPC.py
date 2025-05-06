import tkinter as tk
from tkinter import ttk

# Craemos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

# Manejo de grid (rejilla o cuadricula)
boton1 = ttk.Button(ventana, text='Boton1')
boton2 = ttk.Button(ventana, text='Boton2')
boton3 = ttk.Button(ventana, text='Boton3')

# Publicando de manera horizontal
# boton1.grid(row=0, column=0)
# boton2.grid(row=0, column=1)
# boton3.grid(row=0, column=2)

# Publicar de manera vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

# Publicar en diagonal
boton1.grid(row=0, column=0)
boton2.grid(row=1, column=1)
boton3.grid(row=2, column=2)


ventana.mainloop()

