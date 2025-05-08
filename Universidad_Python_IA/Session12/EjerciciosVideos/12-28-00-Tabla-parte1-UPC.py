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