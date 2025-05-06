import tkinter as tk

# Craemos una ventana
ventana = tk.Tk()

# Redimensionar la ventana
ventana.geometry('600x400')

# Modificar el titulo
ventana.title('Nueva Ventana')

# Evitar redimensionar la ventana
ventana.resizable(0,0)

# Color de la ventana
ventana.configure(background='#1d2d44')

# Hacemos visible la ventana
ventana.mainloop()

