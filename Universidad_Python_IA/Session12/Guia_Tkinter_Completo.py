"""
Guía Completa de Tkinter - Código Unificado
"""

# ======= 12-02-00-CreacionVentana-UPC.py ========
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



# ======= 12-03-00-Etiquetas-UPC.py ========
import tkinter as tk
from tkinter import ttk

# Craemos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

# Creamos una etiqueta (label)
etiqueta = ttk.Label(ventana, text='Saludos')

# Cambiar el texto usando el metodo configure
etiqueta.configure(text='Nos vemos...')

# Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'Adios'

# Publicamos el componente
etiqueta.pack(pady=20)

ventana.mainloop()



# ======= 12-04-00-Botones-UPC.py ========
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



# ======= 12-05-00-CajaTexto-UPC.py ========
import tkinter as tk
from tkinter import ttk

# Craemos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

def mostrar():
    texto = caja_texto.get()  # recuperamos el valor de la caja de texto
    print(f'Texto proporcionado: {texto}')
    etiqueta['text'] = texto

# Caja de texto
caja_texto = ttk.Entry(ventana, font=('Arial', 15))
caja_texto.pack(pady=20)

# Agregar un boton
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack(pady=20)

# Agregamos una etiqueta
etiqueta = ttk.Label(ventana, text='Valor inicial')
etiqueta.pack(pady=20)

ventana.mainloop()



# ======= 12-06-00-Grid-parte1-UPC.py ========
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



# ======= 12-07-00-Grid-configuracion-UPC.py ========
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

# Configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)


# Publicando de manera horizontal
# boton1.grid(row=0, column=0)
# boton2.grid(row=0, column=1)
# boton3.grid(row=0, column=2)

# Publicar de manera vertical
boton1.grid(row=0, column=0)
boton2.grid(row=1, column=0)
boton3.grid(row=2, column=0)

# Publicar en diagonal
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)


ventana.mainloop()



# ======= 12-08-00-Grid-Coordenadas-UPC.py ========
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

# Configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)

# Publicando de manera horizontal
boton1.grid(row=0, column=0, sticky=tk.NSEW)
boton2.grid(row=0, column=1, sticky=tk.SE)
boton3.grid(row=0, column=2, sticky=tk.NW)

# Publicar de manera vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

# Publicar en diagonal
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)


ventana.mainloop()



# ======= 12-09-00-Grid-Margenes-UPC.py ========
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

# Configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)

# Publicando de manera horizontal
boton1.grid(row=0, column=0, padx=20, pady=20, ipadx=30, ipady =30)
boton2.grid(row=0, column=1, sticky=tk.SE, ipadx= 20, ipady=20)
boton3.grid(row=0, column=2, sticky=tk.NW)

# Publicar de manera vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

# Publicar en diagonal
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)


ventana.mainloop()



# ======= 12-10-00-Login-parte1-UPC.py ========
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
# Grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Agregamos un frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0)

frame.grid(row=0, column=0)

ventana.mainloop()

# ======= 12-11-00-Login-parte2-UPC.py ========
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
# Grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Agregamos un frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)

# usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# password
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*')
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

frame.grid(row=0, column=0)

ventana.mainloop()

# ======= 12-12-00-Login-parte3-estilos-UPC.py ========
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
# Grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Creamos un estilo
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black')
estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active', '#0a9396')])

# Agregamos un frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)

# usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# password
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*')
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

frame.grid(row=0, column=0)

ventana.mainloop()

# ======= 12-13-00-Login-parte4-eventos-UPC.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
# Grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Creamos un estilo
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black')
estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active', '#0a9396')])

# Agregamos un frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)

# usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# password
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*')
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def validar(event):
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    # usuario = root y password = admin son los valores correctos
    if usuario == 'root' and password == 'admin':
        showinfo(title='Login', message='Datos correctos!')
    else:
        showerror(title='Login', message='Datos incorrectos!')

# asociar eventos al boton de login
login_boton.bind('<Return>', validar)  # presionar la tecla de enter
login_boton.bind('<Button-1>', validar) # click izquierdo del mouse

frame.grid(row=0, column=0)

ventana.mainloop()

# ======= 12-15-00-AppLoginChatGPT-UPC.py ========
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


# ======= 12-16-00-ManejoTablas-parte1-UPC.py ========
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

# ======= 12-17-00-ManejoTablas-parte2-UPC.py ========
import tkinter as tk
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de Tabla')

# configurar el grid
ventana.columnconfigure(0, weight=1)

#Definir las columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# Cabeceros a la tabla
tabla.heading('Id', text='Id', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# Formato a las columnas
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# Cargar datos a la tabla
datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)

# Publicamos la tabla
tabla.grid(row=0, column=0, sticky=tk.NSEW)

ventana.mainloop()

# ======= 12-18-00-ManejoTablas-parte3-UPC.py ========
import tkinter as tk
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de Tabla')

# configurar el grid
ventana.columnconfigure(0, weight=1)

# Definir un estilo
estilos = ttk.Style()
estilos.theme_use('clam') # prepara el manejo del tema oscuro
estilos.configure('Treeview', background='black',
                  foreground='white',
                  fieldbackground='black',
                  rowheight=30)
estilos.map('Treeview', background=[('selected', '#3a86ff')])

#Definir las columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# Cabeceros a la tabla
tabla.heading('Id', text='Id', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# Formato a las columnas
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# Cargar datos a la tabla
datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)

# Publicamos la tabla
tabla.grid(row=0, column=0, sticky=tk.NSEW)

ventana.mainloop()

# ======= 12-19-00-ManejoTablas-parte4-UPC.py ========
import tkinter as tk
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de Tabla')

# configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)

# Definir un estilo
estilos = ttk.Style()
estilos.theme_use('clam') # prepara el manejo del tema oscuro
estilos.configure('Treeview', background='black',
                  foreground='white',
                  fieldbackground='black',
                  rowheight=30)
estilos.map('Treeview', background=[('selected', '#3a86ff')])

#Definir las columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# Cabeceros a la tabla
tabla.heading('Id', text='Id', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# Formato a las columnas
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# Cargar datos a la tabla
datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))
# datos = ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32))
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)

# Agregamos un scrollbar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# Publicamos la tabla
tabla.grid(row=0, column=0, sticky=tk.NSEW)

ventana.mainloop()

# ======= 12-20-00-ManejoTablas-parte5-UPC.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de Tabla')

# configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)

# Definir un estilo
estilos = ttk.Style()
estilos.theme_use('clam') # prepara el manejo del tema oscuro
estilos.configure('Treeview', background='black',
                  foreground='white',
                  fieldbackground='black',
                  rowheight=30)
estilos.map('Treeview', background=[('selected', '#3a86ff')])

#Definir las columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# Cabeceros a la tabla
tabla.heading('Id', text='Id', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# Formato a las columnas
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# Cargar datos a la tabla
datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))
# datos = ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32))
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)

# Agregamos un scrollbar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# Mostrar registro seleccionado
def mostrar_registro_seleccionado(event):
    print('Ejecutando metodo mostrar_registro_seleccionado')
    elemento_seleccionado = tabla.selection()[0] # solo procesamos el primer registro
    elemento = tabla.item(elemento_seleccionado) # item
    persona = elemento['values']  # tupla de persona
    print(persona)
    showinfo(title='Persona Seleccionada', message=f'Persona: {persona}')

# asociar el evento select de la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_registro_seleccionado)

# Publicamos la tabla
tabla.grid(row=0, column=0, sticky=tk.NSEW)

ventana.mainloop()

# ======= 12-22-00-VentanasPOO-parte1-UPC.py ========
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__() # constructor de la clase padre Tk
        # configurar la ventana
        self.configurar_ventana()
        # configurar el grid
        self.configurar_grid()

    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='#1d2d44')
        self.title('Manejo de Ventanas con POO')


    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-23-00-VentanasPOO-parte2-tabla-UPC.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__() # constructor de la clase padre Tk
        # configurar la ventana
        self.configurar_ventana()
        # configurar el grid
        self.configurar_grid()
        # mostrar la tabla
        self.mostrar_tabla()


    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='#1d2d44')
        self.title('Manejo de Ventanas con POO')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

    def mostrar_tabla(self):
        # Definir un estilo
        estilos = ttk.Style()
        estilos.theme_use('clam')  # prepara el manejo del tema oscuro
        estilos.configure('Treeview', background='black',
                          foreground='white',
                          fieldbackground='black',
                          rowheight=30)
        estilos.map('Treeview', background=[('selected', '#3a86ff')])

        # Definir las columnas
        columnas = ('Id', 'Nombre', 'Edad')
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')

        # Cabeceros a la tabla
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Edad', text='Edad', anchor=tk.W)

        # Formato a las columnas
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)

        # Cargar datos a la tabla
        datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))
        # datos = ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32))
        for persona in datos:
            self.tabla.insert(parent='', index=tk.END, values=persona)

        # Agregamos un scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # asociar el evento select de la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)


    # Mostrar registro seleccionado
    def mostrar_registro_seleccionado(self, event):
        print('Ejecutando metodo mostrar_registro_seleccionado')
        elemento_seleccionado = self.tabla.selection()[0]  # solo procesamos el primer registro
        elemento = self.tabla.item(elemento_seleccionado)  # item
        persona = elemento['values']  # tupla de persona
        print(persona)
        showinfo(title='Persona Seleccionada', message=f'Persona: {persona}')


if __name__ == '__main__':
    app = App()
    app.mainloop()


# ======= 12-25-00-ConfiguracionProyectoZonaFitGUI-UPC/zona_fit_gui/cliente.py ========
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')


# ======= 12-25-00-ConfiguracionProyectoZonaFitGUI-UPC/zona_fit_gui/cliente_dao.py ========
from zona_fit_db.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    cliente_eliminar = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

# ======= 12-25-00-ConfiguracionProyectoZonaFitGUI-UPC/zona_fit_gui/conexion.py ========
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')


# ======= 12-26-00-CreacionVentanaZonaFit-UPC.py ========
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-27-00-TituloZonaFit-UPC.py ========
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 15),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-28-00-Tabla-parte1-UPC.py ========
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 15),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        pass

    def mostrar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresía')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-29-00-Tabla-parte2-UPC/zona_fit_gui/cliente.py ========
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')


# ======= 12-29-00-Tabla-parte2-UPC/zona_fit_gui/cliente_dao.py ========
from zona_fit_gui.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    cliente_eliminar = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

# ======= 12-29-00-Tabla-parte2-UPC/zona_fit_gui/conexion.py ========
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')


# ======= 12-29-00-Tabla-parte2-UPC/zona_fit_gui/zona_fit_app_gui.py ========
import tkinter as tk
from tkinter import ttk

from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 15),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        pass

    def mostrar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-30-00-Tabla-parte3-scrollbar-UPC.py ========
import tkinter as tk
from tkinter import ttk

from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 15),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        pass

    def mostrar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-31-00-Formulario-parte1-UPC.py ========
import tkinter as tk
from tkinter import ttk

from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 15),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-32-00-Botones-UPC.py ========
import tkinter as tk
from tkinter import ttk

from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        pass

    def eliminar_cliente(self):
        pass

    def limpiar_datos(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-33-00-BotonesEstilos-UPC.py ========
import tkinter as tk
from tkinter import ttk

from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Aplicar un estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        pass

    def eliminar_cliente(self):
        pass

    def limpiar_datos(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-34-00-ValidacionFormulario-UPC/zona_fit_gui/cliente.py ========
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')


# ======= 12-34-00-ValidacionFormulario-UPC/zona_fit_gui/cliente_dao.py ========
from zona_fit_gui.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    cliente_eliminar = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

# ======= 12-34-00-ValidacionFormulario-UPC/zona_fit_gui/conexion.py ========
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')


# ======= 12-34-00-ValidacionFormulario-UPC/zona_fit_gui/zona_fit_app_gui.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Aplicar un estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        # Validar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion',
                          message='El valor de membresía NO es numérico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atencion', message='Debe llenar el formulario')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        pass

    def eliminar_cliente(self):
        pass

    def limpiar_datos(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-35-00-GuardarNuevoCliente-UPC/zona_fit_gui/cliente.py ========
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')


# ======= 12-35-00-GuardarNuevoCliente-UPC/zona_fit_gui/cliente_dao.py ========
from zona_fit_gui.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    cliente_eliminar = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

# ======= 12-35-00-GuardarNuevoCliente-UPC/zona_fit_gui/conexion.py ========
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')


# ======= 12-35-00-GuardarNuevoCliente-UPC/zona_fit_gui/zona_fit_app_gui.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from zona_fit_gui.cliente import Cliente
from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def cargar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Aplicar un estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        # Validar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion',
                          message='El valor de membresía NO es numérico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atencion', message='Debe llenar el formulario')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        # Recuperar los valores de las cajas de texto
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        ClienteDAO.insertar(cliente)
        showinfo(title='Agregar', message='Cliente agregado...')
        # Volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()

    def recargar_datos(self):
        # Volver a cargar los datos de la tabla
        self.cargar_tabla()
        # Limpiar los datos
        self.limpiar_datos()


    def eliminar_cliente(self):
        pass

    def limpiar_datos(self):
        self.limpiar_formulario()

    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-36-00-CargarCliente-UPC/zona_fit_gui/cliente.py ========
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')


# ======= 12-36-00-CargarCliente-UPC/zona_fit_gui/cliente_dao.py ========
from zona_fit_gui.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    cliente_eliminar = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

# ======= 12-36-00-CargarCliente-UPC/zona_fit_gui/conexion.py ========
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')


# ======= 12-36-00-CargarCliente-UPC/zona_fit_gui/zona_fit_app_gui.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from zona_fit_gui.cliente import Cliente
from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def cargar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Asociar el evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Aplicar un estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        # Validar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion',
                          message='El valor de membresía NO es numérico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atencion', message='Debe llenar el formulario')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        # Recuperar los valores de las cajas de texto
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        ClienteDAO.insertar(cliente)
        showinfo(title='Agregar', message='Cliente agregado...')
        # Volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values']  # tupla de valores del cliente seleccionado
        # Recuperar cada valor del cliente
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        # Antes de cargar, limpiamos el formulario
        self.limpiar_formulario()
        # Cargar los valores en el formulario
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    def recargar_datos(self):
        # Volver a cargar los datos de la tabla
        self.cargar_tabla()
        # Limpiar los datos
        self.limpiar_datos()


    def eliminar_cliente(self):
        pass

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-37-00-Actualizar-UPC/zona_fit_gui/cliente.py ========
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')


# ======= 12-37-00-Actualizar-UPC/zona_fit_gui/cliente_dao.py ========
from zona_fit_gui.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    cliente_eliminar = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

# ======= 12-37-00-Actualizar-UPC/zona_fit_gui/conexion.py ========
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')


# ======= 12-37-00-Actualizar-UPC/zona_fit_gui/zona_fit_app_gui.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from zona_fit_gui.cliente import Cliente
from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def cargar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Asociar el evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Aplicar un estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        # Validar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion',
                          message='El valor de membresía NO es numérico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atencion', message='Debe llenar el formulario')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        # Recuperar los valores de las cajas de texto
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        # Validamos el valor del self.id_cliente
        if self.id_cliente is None:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Agregar', message='Cliente agregado...')
        else:  # Actualizar
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualizar', message='Cliente actualizado...')
        # Volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values']  # tupla de valores del cliente seleccionado
        # Recuperar cada valor del cliente
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        # Antes de cargar, limpiamos el formulario
        self.limpiar_formulario()
        # Cargar los valores en el formulario
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    def recargar_datos(self):
        # Volver a cargar los datos de la tabla
        self.cargar_tabla()
        # Limpiar los datos
        self.limpiar_datos()

    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Atención',
                      message='Debes seleccionar un cliente a eliminar')
        else:
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Eliminado', message='Cliente eliminado...')
            self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)


if __name__ == '__main__':
    app = App()
    app.mainloop()

# ======= 12-38-00-Eliminar-UPC/zona_fit_gui/cliente.py ========
class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')


# ======= 12-38-00-Eliminar-UPC/zona_fit_gui/cliente_dao.py ========
from zona_fit_gui.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    cliente_eliminar = Cliente(id=3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

# ======= 12-38-00-Eliminar-UPC/zona_fit_gui/conexion.py ========
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')


# ======= 12-38-00-Eliminar-UPC/zona_fit_gui/zona_fit_app_gui.py ========
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from zona_fit_gui.cliente import Cliente
from zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_forma = ttk.Frame()
        # Nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)

        # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)

    def cargar_tabla(self):
        # Creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        # Definimos las columnas
        columnas = ('Id', 'Nombre', 'Apellido','Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # Agregar los cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        # Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        # Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                                      cliente.apellido, cliente.membresia))

        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Asociar el evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear los botones
        # Boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        # Boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        # Aplicar un estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        # Validar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion',
                          message='El valor de membresía NO es numérico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atencion', message='Debe llenar el formulario')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        # Recuperar los valores de las cajas de texto
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        # Validamos el valor del self.id_cliente
        if self.id_cliente is None:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Agregar', message='Cliente agregado...')
        else:  # Actualizar
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualizar', message='Cliente actualizado...')
        # Volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values']  # tupla de valores del cliente seleccionado
        # Recuperar cada valor del cliente
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        # Antes de cargar, limpiamos el formulario
        self.limpiar_formulario()
        # Cargar los valores en el formulario
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    def recargar_datos(self):
        # Volver a cargar los datos de la tabla
        self.cargar_tabla()
        # Limpiar los datos
        self.limpiar_datos()

    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Atención',
                      message='Debes seleccionar un cliente a eliminar')
        else:
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Eliminado', message='Cliente eliminado...')
            self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)


if __name__ == '__main__':
    app = App()
    app.mainloop()

