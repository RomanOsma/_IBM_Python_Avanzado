import tkinter as tk
from tkinter import ttk

# Craemos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

def saludar(nombre):
    print(f'Saludos {nombre}')

# Botones
boton1 = ttk.Button(ventana, text='Enviar', command=lambda: saludar('Juan'))
boton1.pack(pady=20)

ventana.mainloop()

