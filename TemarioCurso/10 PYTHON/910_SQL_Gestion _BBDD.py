import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class DatabaseManager:
    """
    Clase responsable de la conexión y operaciones CRUD contra la BBDD MySQL 'cursosql'.
    """
    def __init__(self):
        # Conexión MySQL al iniciar
        self.cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='cursosql'
        )
        # Cursor en modo diccionario para acceder por nombre de columna
        self.cursor = self.cnx.cursor(dictionary=True)

    def fetch_all(self, table):
        """Recupera todos los registros de la tabla especificada."""
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()

    def insert(self, table, data):
        """Inserta un registro en 'table'. 'data' es dict columna: valor."""
        cols = ", ".join(data.keys())
        vals = tuple(data.values())
        placeholders = ", ".join(["%s"] * len(vals))
        sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
        self.cursor.execute(sql, vals)
        self.cnx.commit()

    def update(self, table, key_col, key_val, data):
        """Actualiza campos de 'table' donde key_col=key_val con los valores en 'data'."""
        assignments = ", ".join([f"{col}=%s" for col in data.keys()])
        vals = tuple(data.values()) + (key_val,)
        sql = f"UPDATE {table} SET {assignments} WHERE {key_col} = %s"
        self.cursor.execute(sql, vals)
        self.cnx.commit()

    def delete(self, table, key_col, key_val):
        """Elimina el registro de 'table' donde key_col=key_val."""
        sql = f"DELETE FROM {table} WHERE {key_col} = %s"
        self.cursor.execute(sql, (key_val,))
        self.cnx.commit()

    def close(self):
        """Cierra cursor y conexión."""
        self.cursor.close()
        self.cnx.close()

class App(tk.Tk):
    """
    Interfaz gráfica mejorada y profesional para gestionar CRUD de las tablas.
    Usa ttk.Notebook con estilo moderno y Treeview con filas alternadas.
    """
    def __init__(self):
        super().__init__()
        self.title("Gestor CursosQL • Profesional")
        self.geometry("900x650")
        self.configure(bg="#f0f0f0")

        # Configuración de estilo
        style = ttk.Style(self)
        style.theme_use("clam")
        # Estilos globales
        style.configure(".", background="#f0f0f0", foreground="#333333", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#4a4a4a", foreground="white")
        style.configure("Treeview", rowheight=24, font=("Segoe UI", 10))
        style.map("Treeview.Heading", relief=[('active','raised')])
        style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))
        style.configure("Accent.TButton", foreground="white", background="#007acc")
        style.map("Accent.TButton", background=[("active", "#005f99")])

        # Conexión a la base de datos
        self.db = DatabaseManager()

        # Pestañas
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.frames = {}
        for table in ('clientes', 'articulos', 'pedidos'):
            frame = CRUDFrame(notebook, table, self.db)
            notebook.add(frame, text=table.capitalize())
            self.frames[table] = frame

        # Evento de cierre
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.db.close()
        self.destroy()

class CRUDFrame(ttk.Frame):
    """
    Frame genérico con Treeview, formulario y botones CRUD mejorados.
    """
    def __init__(self, parent, table, db_manager):
        super().__init__(parent, padding=10)
        self.table = table
        self.db = db_manager

        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # 1) Sección de Treeview
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=0, column=0, sticky="nsew")
        columns = self._get_columns()
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings', selectmode='browse')
        # Scrollbars
        vsb = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        hsb = ttk.Scrollbar(tree_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')
        self.tree.pack(fill='both', expand=True)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='w')
        # Filas alternadas
        self.tree.tag_configure('oddrow', background='#f9f9f9')
        self.tree.tag_configure('evenrow', background='#e0e0e0')
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        # 2) Sección de formulario
        form_frame = ttk.LabelFrame(self, text='Detalles', padding=10)
        form_frame.grid(row=1, column=0, sticky='ew', pady=10)
        self.entries = {}
        for idx, col in enumerate(columns):
            ttk.Label(form_frame, text=col).grid(row=idx, column=0, sticky='e', pady=2, padx=5)
            ent = ttk.Entry(form_frame)
            ent.grid(row=idx, column=1, sticky='ew', pady=2, padx=5)
            form_frame.columnconfigure(1, weight=1)
            self.entries[col] = ent

        # 3) Sección de botones
        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=2, column=0, sticky='e')
        ttk.Button(btn_frame, text='Create', command=self.create, style='Accent.TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text='Update', command=self.update).pack(side='left', padx=5)
        ttk.Button(btn_frame, text='Delete', command=self.delete).pack(side='left', padx=5)
        ttk.Button(btn_frame, text='Refresh', command=self.refresh).pack(side='left', padx=5)

        # Carga inicial
        self.refresh()

    def _get_columns(self):
        """Nombres de columnas según la tabla."""
        if self.table == 'clientes':
            return ['codigoCliente','empresa','direccion','poblacion','telefono','responsable','historial']
        if self.table == 'articulos':
            return ['codigo_articulo','seccion','nombre_articulo','precio','fecha','importado','pais_origen','foto']
        if self.table == 'pedidos':
            return ['id_pedido','codigoCliente','codigo_articulo','cantidad','fecha_pedido']

    def refresh(self):
        """Recarga datos en el Treeview con filas alternadas."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = self.db.fetch_all(self.table)
        for idx, fila in enumerate(rows):
            values = [fila[col] for col in self._get_columns()]
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            self.tree.insert('', tk.END, values=values, tags=(tag,))

    def on_select(self, event):
        """Carga los datos seleccionados en el formulario."""
        sel = self.tree.selection()
        if not sel: return
        values = self.tree.item(sel[0], 'values')
        for col, val in zip(self._get_columns(), values):
            self.entries[col].delete(0, tk.END)
            self.entries[col].insert(0, val)

    def create(self):
        """Inserta un nuevo registro con los datos del formulario."""
        data = {col: self.entries[col].get() for col in self._get_columns() if col != 'id_pedido'}
        try:
            self.db.insert(self.table, data)
            messagebox.showinfo('Success', 'Registro creado')
            self.refresh()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def update(self):
        """Actualiza el registro seleccionado usando la PK."""
        pk = self._get_columns()[0]
        key_val = self.entries[pk].get()
        data = {col: self.entries[col].get() for col in self._get_columns() if col != pk}
        try:
            self.db.update(self.table, pk, key_val, data)
            messagebox.showinfo('Success', 'Registro actualizado')
            self.refresh()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def delete(self):
        """Elimina el registro seleccionado tras confirmación."""
        pk = self._get_columns()[0]
        key_val = self.entries[pk].get()
        if messagebox.askyesno('Confirm', '¿Seguro que quieres eliminar?'):
            try:
                self.db.delete(self.table, pk, key_val)
                messagebox.showinfo('Success', 'Registro eliminado')
                self.refresh()
            except Exception as e:
                messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    app = App()
    app.mainloop()