import tkinter as tk
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de Tabla')

#Definir las columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# Cabeceros a la tabla
tabla.heading('Id', text='Id')
tabla.heading('Nombre', text='Nombre')
tabla.heading('Edad', text='Edad')

# Formato a las columnas
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# Cargar datos a la tabla
datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)

# Publicamos la tabla
tabla.grid(row=0, column=0)

ventana.mainloop()