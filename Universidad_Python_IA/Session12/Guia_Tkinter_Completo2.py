import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

def ejemplo_creacion_ventana():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.resizable(0,0)
    win.configure(background='#1d2d44')

def ejemplo_etiquetas():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    etiqueta = ttk.Label(win, text='Saludos')
    etiqueta.configure(text='Nos vemos...')
    etiqueta['text'] = 'Adios'
    etiqueta.pack(pady=20)

def ejemplo_botones():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    def saludar(nombre):
        print(f'Saludos {nombre}')
    boton1 = ttk.Button(win, text='Enviar', command=lambda: saludar('Juan'))
    boton1.pack(pady=20)

def ejemplo_caja_texto():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    def mostrar():
        texto = caja_texto.get()
        print(f'Texto proporcionado: {texto}')
        etiqueta['text'] = texto
    caja_texto = ttk.Entry(win, font=('Arial', 15))
    caja_texto.pack(pady=20)
    boton = ttk.Button(win, text='Enviar', command=mostrar)
    boton.pack(pady=20)
    etiqueta = ttk.Label(win, text='Valor inicial')
    etiqueta.pack(pady=20)

def ejemplo_grid_parte1():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    boton1 = ttk.Button(win, text='Boton1')
    boton2 = ttk.Button(win, text='Boton2')
    boton3 = ttk.Button(win, text='Boton3')
    # Publicar en diagonal
    boton1.grid(row=0, column=0)
    boton2.grid(row=1, column=1)
    boton3.grid(row=2, column=2)

def ejemplo_grid_configuracion():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    boton1 = ttk.Button(win, text='Boton1')
    boton2 = ttk.Button(win, text='Boton2')
    boton3 = ttk.Button(win, text='Boton3')
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    # Publicar de manera vertical
    boton1.grid(row=0, column=0)
    boton2.grid(row=1, column=0)
    boton3.grid(row=2, column=0)

def ejemplo_grid_coordenadas():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    boton1 = ttk.Button(win, text='Boton1')
    boton2 = ttk.Button(win, text='Boton2')
    boton3 = ttk.Button(win, text='Boton3')
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    boton1.grid(row=0, column=0, sticky=tk.NSEW)
    boton2.grid(row=0, column=1, sticky=tk.SE)
    boton3.grid(row=0, column=2, sticky=tk.NW)

def ejemplo_grid_margenes():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    boton1 = ttk.Button(win, text='Boton1')
    boton2 = ttk.Button(win, text='Boton2')
    boton3 = ttk.Button(win, text='Boton3')
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    boton1.grid(row=0, column=0, padx=20, pady=20, ipadx=30, ipady=30)
    boton2.grid(row=0, column=1, sticky=tk.SE, ipadx=20, ipady=20)
    boton3.grid(row=0, column=2, sticky=tk.NW)

def ejemplo_tablas_parte1():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    #Definir las columnas
    columnas = ('Id', 'Nombre', 'Edad')
    tabla = ttk.Treeview(win, columns=columnas, show='headings')
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
    tabla.pack(pady=30)

def ejemplo_tablas_parte2():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    # configurar el grid
    win.columnconfigure(0, weight=1)
    #Definir las columnas
    columnas = ('Id', 'Nombre', 'Edad')
    tabla = ttk.Treeview(win, columns=columnas, show='headings')
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

def ejemplo_tablas_parte3():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    # configurar el grid
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    #Definir las columnas
    columnas = ('Id', 'Nombre', 'Edad')
    tabla = ttk.Treeview(win, columns=columnas, show='headings')
    # Cabeceros a la tabla
    tabla.heading('Id', text='Id', anchor=tk.CENTER)
    tabla.heading('Nombre', text='Nombre', anchor=tk.W)
    tabla.heading('Edad', text='Edad', anchor=tk.W)
    # Formato a las columnas
    tabla.column('Id', width=80, anchor=tk.CENTER)
    tabla.column('Nombre', width=120, anchor=tk.W)
    tabla.column('Edad', width=120, anchor=tk.W)
    # Cargar datos a la tabla
    datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))
    for persona in datos:
        tabla.insert(parent='', index=tk.END, values=persona)
    # Scrollbar vertical
    scroll_vertical = ttk.Scrollbar(win, orient='vertical', command=tabla.yview)
    tabla.configure(yscrollcommand=scroll_vertical.set)
    # Publicamos la tabla
    tabla.grid(row=0, column=0, sticky=tk.NSEW)
    scroll_vertical.grid(row=0, column=1, sticky=tk.NS)

def ejemplo_login_parte1():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    # Grid de la ventana
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    # Agregamos un frame
    frame = ttk.Frame(win)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=3)
    # titulo
    etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
    etiqueta.grid(row=0, column=0)
    frame.grid(row=0, column=0)

def ejemplo_login_parte2():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    # Grid de la ventana
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    # Agregamos un frame
    frame = ttk.Frame(win)
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

def ejemplo_login_parte3():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    # Grid de la ventana
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    # Creamos un estilo
    estilos = ttk.Style()
    estilos.theme_use('clam')
    estilos.configure(win, background='#1d2d44', foreground='white', fieldbackground='black')
    estilos.configure('TButton', background='#005f73')
    estilos.map('TButton', background=[('active', '#0a9396')])
    # Agregamos un frame
    frame = ttk.Frame(win)
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

def ejemplo_login_parte4():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d2d44')
    # Grid de la ventana
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)
    # Creamos un estilo
    estilos = ttk.Style()
    estilos.theme_use('clam')
    estilos.configure(win, background='#1d2d44', foreground='white', fieldbackground='black')
    estilos.configure('TButton', background='#005f73')
    estilos.map('TButton', background=[('active', '#0a9396')])
    # Agregamos un frame
    frame = ttk.Frame(win)
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
    login_boton.bind('<Return>', validar) # presionar la tecla de enter
    login_boton.bind('<Button-1>', validar) # click izquierdo del mouse
    frame.grid(row=0, column=0)

def ejemplo_login_chatgpt():
    win = tk.Toplevel()
    win.geometry('600x400')
    win.title('Nueva Ventana')
    win.configure(background='#1d1d1d')
    # Crear ventana principal
    # Aplicar tema oscuro
    estilo = ttk.Style()
    estilo.theme_use('clam')
    estilo.configure('.', background='#1d1d1d', foreground='white')
    estilo.configure('TButton', background='#005f73')
    estilo.map('TButton', background=[('active', '#0a9396')])
    # Crear frame para el formulario
    frame = ttk.Frame(win, padding=(20, 20))
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
    def validar():
        usuario = usuario_caja_texto.get()
        password = password_caja_texto.get()
        if usuario == 'root' and password == 'admin':
            showinfo(title='Login', message='¡Datos correctos!')
        else:
            showerror(title='Login', message='¡Datos incorrectos!')
    enviar_boton = ttk.Button(frame, text='Enviar', command=validar)
    enviar_boton.grid(row=3, column=0, columnspan=2, pady=10)

# Ventana principal y menú
root = tk.Tk()
root.title('Menú de Ejemplos Tkinter')
root.geometry('800x600')

menubar = tk.Menu(root)

# Menú de ejemplos básicos
ejemplos_menu = tk.Menu(menubar, tearoff=0)
ejemplos_menu.add_command(label='Creación de Ventana', command=ejemplo_creacion_ventana)
ejemplos_menu.add_command(label='Etiquetas', command=ejemplo_etiquetas)
ejemplos_menu.add_command(label='Botones', command=ejemplo_botones)
ejemplos_menu.add_command(label='Caja de Texto', command=ejemplo_caja_texto)
menubar.add_cascade(label='Ejemplos Básicos', menu=ejemplos_menu)

# Menú de ejemplos de Grid
grid_menu = tk.Menu(menubar, tearoff=0)
grid_menu.add_command(label='Grid Parte 1', command=ejemplo_grid_parte1)
grid_menu.add_command(label='Grid Configuración', command=ejemplo_grid_configuracion)
grid_menu.add_command(label='Grid Coordenadas', command=ejemplo_grid_coordenadas)
grid_menu.add_command(label='Grid Márgenes', command=ejemplo_grid_margenes)
menubar.add_cascade(label='Ejemplos Grid', menu=grid_menu)

# Menú de ejemplos de Login
login_menu = tk.Menu(menubar, tearoff=0)
login_menu.add_command(label='Login Parte 1', command=ejemplo_login_parte1)
login_menu.add_command(label='Login Parte 2', command=ejemplo_login_parte2)
login_menu.add_command(label='Login Parte 3 (Estilos)', command=ejemplo_login_parte3)
login_menu.add_command(label='Login Parte 4 (Eventos)', command=ejemplo_login_parte4)
login_menu.add_command(label='App Login ChatGPT', command=ejemplo_login_chatgpt)
menubar.add_cascade(label='Ejemplos Login', menu=login_menu)

# Menú de ejemplos de Tablas
tablas_menu = tk.Menu(menubar, tearoff=0)
tablas_menu.add_command(label='Tablas Parte 1', command=ejemplo_tablas_parte1)
tablas_menu.add_command(label='Tablas Parte 2', command=ejemplo_tablas_parte2)
tablas_menu.add_command(label='Tablas Parte 3', command=ejemplo_tablas_parte3)
menubar.add_cascade(label='Ejemplos Tablas', menu=tablas_menu)

menubar.add_command(label='Salir', command=root.destroy)
root.config(menu=menubar)

root.mainloop()
