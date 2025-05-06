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
