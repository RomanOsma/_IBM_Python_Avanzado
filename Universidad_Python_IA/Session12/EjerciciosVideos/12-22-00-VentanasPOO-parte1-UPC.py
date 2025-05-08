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