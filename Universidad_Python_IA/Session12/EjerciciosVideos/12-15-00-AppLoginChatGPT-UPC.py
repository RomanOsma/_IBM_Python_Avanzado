import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


def validar():
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    if usuario == 'root' and password == 'admin':
        showinfo(title='Login', message='¡Datos correctos!')
    else:
        showerror(title='Login', message='¡Datos incorrectos!')

# Crear ventana principal
ventana = tk.Tk()
ventana.title('Login')

# Aplicar tema oscuro
ventana.configure(bg='#1d1d1d')
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('.', background='#1d1d1d', foreground='white')
estilo.configure('TButton', background='#005f73')
estilo.map('TButton', background=[('active', '#0a9396')])

# Crear frame para el formulario
frame = ttk.Frame(ventana, padding=(20, 20))
frame.grid(row=0, column=0, padx=50, pady=50)

# Título del formulario
titulo = ttk.Label(frame, text='Login', font=('Arial', 20))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Etiqueta y caja de texto para el usuario
usuario_label = ttk.Label(frame, text='Usuario:')
usuario_label.grid(row=1, column=0, sticky='w', pady=5)
usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky='e', pady=5)
# Configurar color oscuro de fondo para la caja de texto de usuario
estilo.configure('TEntry', fieldbackground='#424242')

# Etiqueta y caja de texto para la contraseña
password_label = ttk.Label(frame, text='Password:')
password_label.grid(row=2, column=0, sticky='w', pady=5)
password_caja_texto = ttk.Entry(frame, show='*')
password_caja_texto.grid(row=2, column=1, sticky='e', pady=5)
# Configurar color oscuro de fondo para la caja de texto de contraseña
estilo.configure('TEntry', fieldbackground='#424242')

# Botón de enviar
enviar_boton = ttk.Button(frame, text='Enviar', command=validar)
enviar_boton.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
