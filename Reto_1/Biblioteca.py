import streamlit as st
import csv
import pandas as pd
from io import StringIO
import requests
from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor, isbn, genero=None, anio_publicacion=None):
        self.titulo = titulo  
        self.autor = autor  
        self.isbn = isbn  
        self.disponible = True
        self.genero = genero or "No especificado"
        self.anio_publicacion = anio_publicacion
        self.fecha_prestamo = None
        self.prestado_a = None

    def prestar(self, nombre_prestatario, dias_prestamo=14):
        if self.disponible:
            self.disponible = False
            self.fecha_prestamo = datetime.now()
            self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias_prestamo)
            self.prestado_a = nombre_prestatario
            return True, f'Libro "{self.titulo}" prestado a {nombre_prestatario}. Devolver antes del {self.fecha_devolucion.strftime("%d/%m/%Y")}.'
        return False, f'El libro "{self.titulo}" ya está prestado.'

    def devolver(self):
        if not self.disponible:
            mensaje = f'Libro "{self.titulo}" devuelto por {self.prestado_a}.'
            self.disponible = True
            self.fecha_prestamo = None
            self.prestado_a = None
            return True, mensaje
        return False, f'El libro "{self.titulo}" ya estaba disponible.'

    def info_completa(self):
        estado = '✅ Disponible' if self.disponible else f'❌ Prestado a {self.prestado_a} (devolución: {self.fecha_devolucion.strftime("%d/%m/%Y")})'
        return (
            f"**Título:** {self.titulo}\n\n"
            f"**Autor:** {self.autor}\n\n"
            f"**ISBN:** {self.isbn}\n\n"
            f"**Género:** {self.genero}\n\n"
            f"**Año publicación:** {self.anio_publicacion or 'Desconocido'}\n\n"
            f"**Estado:** {estado}"
        )

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.historial = []
        self.isbn_counter = 1000000000  # ISBN de 10 dígitos

    def generar_isbn(self):
        while str(self.isbn_counter) in self.libros:
            self.isbn_counter += 1
        return str(self.isbn_counter)

    def validar_isbn(self, isbn):
        return isbn.isdigit() and len(isbn) in (10, 13)  # ISBN-10 o ISBN-13

    def agregar_libro(self, titulo, autor, isbn=None, genero=None, anio=None):
        if not titulo or not autor:
            return False, "❌ El título y el autor son obligatorios."
            
        if not isbn:
            isbn = self.generar_isbn()
            mensaje_isbn = f"📝 ISBN generado automáticamente: {isbn}"
        elif not self.validar_isbn(isbn):
            return False, f"❌ ISBN inválido. Debe ser 10 o 13 dígitos numéricos."
        else:
            mensaje_isbn = ""

        if isbn in self.libros:
            return False, f"❌ Ya existe un libro con ISBN {isbn}."

        libro = Libro(titulo, autor, isbn, genero, anio)
        self.libros[isbn] = libro
        self.registrar_historial("AGREGADO", f"Libro '{titulo}' agregado")
        return True, f"✅ Libro agregado: {titulo} (ISBN: {isbn})"

    def prestar_libro(self, isbn, prestatario, dias=14):
        libro = self.libros.get(isbn)
        if not libro:
            return False, f"❌ Libro con ISBN {isbn} no encontrado."
        
        exito, mensaje = libro.prestar(prestatario, dias)
        if exito:
            self.registrar_historial("PRÉSTAMO", f"Libro '{libro.titulo}' prestado a {prestatario}")
        return exito, mensaje

    def devolver_libro(self, isbn):
        libro = self.libros.get(isbn)
        if not libro:
            return False, f"❌ Libro con ISBN {isbn} no encontrado."
        
        exito, mensaje = libro.devolver()
        if exito:
            self.registrar_historial("DEVOLUCIÓN", f"Libro '{libro.titulo}' devuelto")
        return exito, mensaje

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            attr = getattr(libro, criterio, "").lower()
            if valor.lower() in attr:
                resultados.append(libro)
        return resultados

    def registrar_historial(self, accion, detalle):
        self.historial.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": accion,
            "detalle": detalle
        })

    def obtener_dataframe_libros(self):
        datos = []
        for libro in self.libros.values():
            datos.append({
                'Título': libro.titulo,
                'Autor': libro.autor,
                'ISBN': libro.isbn,
                'Género': libro.genero,
                'Año': libro.anio_publicacion or '',
                'Disponible': 'Sí' if libro.disponible else 'No',
                'Prestado a': libro.prestado_a or '',
                'Devolución': libro.fecha_devolucion.strftime("%d/%m/%Y") if libro.fecha_devolucion else ''
            })
        return pd.DataFrame(datos)

    def cargar_csv(self, contenido_csv):
        try:
            csv_io = StringIO(contenido_csv)
            df = pd.read_csv(csv_io)
            
            required_cols = {'Title', 'Author'}
            if not required_cols.issubset(df.columns):
                return False, "❌ El CSV debe contener columnas 'Title' y 'Author'"
            
            agregados = 0
            for _, fila in df.iterrows():
                titulo = fila['Title'].strip()
                autor = fila.get('Author', 'Desconocido').strip()
                genero = fila.get('Genre', '').strip()
                anio = fila.get('Year', '').strip()
                isbn = fila.get('ISBN', '').strip()
                
                if titulo:
                    self.agregar_libro(
                        titulo, autor, 
                        isbn if isbn else None,
                        genero if genero else None,
                        anio if anio and anio.isdigit() else None
                    )
                    agregados += 1
            
            self.registrar_historial("IMPORTACIÓN", f"Importados {agregados} libros desde CSV")
            return True, f"✅ {agregados} libros importados correctamente"
        except Exception as e:
            return False, f"❌ Error al procesar CSV: {str(e)}"

# Configuración de la aplicación
def configurar_app():
    st.set_page_config(
        page_title="Biblioteca Digital",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Estilos CSS personalizados
    st.markdown("""
        <style>
            .st-emotion-cache-1kyxreq {justify-content: center;}
            .st-emotion-cache-1v0mbdj {margin: 0 auto;}
            .book-card {border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px 0;}
            .available {background-color: #e6f7e6;}
            .unavailable {background-color: #ffebeb;}
            .header {color: #2e86c1;}
        </style>
    """, unsafe_allow_html=True)

def inicializar_biblioteca():
    if 'biblioteca' not in st.session_state:
        st.session_state.biblioteca = Biblioteca()
        cargar_libros_iniciales(st.session_state.biblioteca)
    return st.session_state.biblioteca

def cargar_libros_iniciales(biblioteca):
    try:
        url = 'https://raw.githubusercontent.com/RomanOsma/Curso-IBM-Python/main/ProyectoFinal/skyrim_books.csv'
        response = requests.get(url)
        response.raise_for_status()
        biblioteca.cargar_csv(response.text)
    except Exception as e:
        st.warning(f"No se pudieron cargar libros iniciales: {e}")

def mostrar_libro(libro):
    estado = "available" if libro.disponible else "unavailable"
    st.markdown(f"""
        <div class="book-card {estado}">
            <h3>{libro.titulo}</h3>
            <p><strong>Autor:</strong> {libro.autor}</p>
            <p><strong>ISBN:</strong> {libro.isbn}</p>
            <p><strong>Estado:</strong> {"Disponible" if libro.disponible else f"Prestado a {libro.prestado_a} (devolución: {libro.fecha_devolucion.strftime('%d/%m/%Y')})"}</p>
        </div>
    """, unsafe_allow_html=True)

def pagina_inicio(biblioteca):
    st.header("🏠 Biblioteca Digital", divider="rainbow")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        busqueda = st.text_input("🔍 Buscar libros:", placeholder="Título, autor o género")
    with col2:
        filtro_disponible = st.selectbox("Filtrar por:", ["Todos", "Disponibles", "Prestados"])
    
    df = biblioteca.obtener_dataframe_libros()
    
    if busqueda:
        resultados = []
        for criterio in ['Título', 'Autor', 'Género']:
            resultados.extend(biblioteca.buscar_libro(criterio.lower(), busqueda))
        df = pd.DataFrame([{
            'Título': l.titulo,
            'Autor': l.autor,
            'ISBN': l.isbn,
            'Disponible': 'Sí' if l.disponible else 'No'
        } for l in resultados])
    
    if filtro_disponible == "Disponibles":
        df = df[df['Disponible'] == 'Sí']
    elif filtro_disponible == "Prestados":
        df = df[df['Disponible'] == 'No']
    
    if df.empty:
        st.info("No se encontraron libros con los criterios seleccionados")
    else:
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "Título": st.column_config.TextColumn(width="large"),
                "Autor": st.column_config.TextColumn(width="medium"),
                "ISBN": st.column_config.TextColumn(width="small"),
                "Disponible": st.column_config.TextColumn(width="small")
            },
            hide_index=True
        )
    
    st.metric("📊 Total de libros", len(biblioteca.libros))
    col1, col2 = st.columns(2)
    col1.metric("📚 Disponibles", sum(1 for l in biblioteca.libros.values() if l.disponible))
    col2.metric("⏳ Prestados", sum(1 for l in biblioteca.libros.values() if not l.disponible))

def pagina_agregar(biblioteca):
    st.header("➕ Agregar Nuevo Libro", divider="rainbow")
    
    with st.form("form_agregar", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            titulo = st.text_input("Título*", help="Título completo del libro")
            autor = st.text_input("Autor*", help="Autor o autores del libro")
        with col2:
            genero = st.text_input("Género", help="Ej: Fantasía, Ciencia Ficción, etc.")
            anio = st.text_input("Año de publicación", help="Año en que se publicó el libro")
        
        isbn_manual = st.checkbox("Especificar ISBN manualmente")
        isbn = st.text_input("ISBN (10 o 13 dígitos)", disabled=not isbn_manual, 
                           help="Dejar en blanco para generar automáticamente") if isbn_manual else ""
        
        if st.form_submit_button("Agregar Libro", use_container_width=True):
            if not titulo or not autor:
                st.error("Los campos marcados con * son obligatorios")
            else:
                exito, mensaje = biblioteca.agregar_libro(
                    titulo, autor, 
                    isbn if isbn_manual else None,
                    genero if genero else None,
                    anio if anio and anio.isdigit() else None
                )
                if exito:
                    st.success(mensaje)
                else:
                    st.error(mensaje)

def pagina_prestamos(biblioteca):
    st.header("🔄 Gestión de Préstamos", divider="rainbow")
    
    tab1, tab2 = st.tabs(["Prestar Libro", "Devolver Libro"])
    
    with tab1:
        st.subheader("📥 Prestar Libro")
        isbn = st.text_input("ISBN del libro", key="prestamo_isbn")
        prestatario = st.text_input("Nombre del prestatario")
        dias = st.slider("Días de préstamo", 7, 30, 14)
        
        if st.button("Registrar Préstamo", key="btn_prestar"):
            if isbn and prestatario:
                exito, mensaje = biblioteca.prestar_libro(isbn, prestatario, dias)
                if exito:
                    st.success(mensaje)
                    st.balloons()
                else:
                    st.error(mensaje)
            else:
                st.warning("Complete todos los campos")
    
    with tab2:
        st.subheader("📤 Devolver Libro")
        isbn = st.text_input("ISBN del libro", key="devolucion_isbn")
        
        if st.button("Registrar Devolución", key="btn_devolver"):
            if isbn:
                exito, mensaje = biblioteca.devolver_libro(isbn)
                if exito:
                    st.success(mensaje)
                else:
                    st.error(mensaje)
            else:
                st.warning("Ingrese el ISBN del libro")

def pagina_buscar(biblioteca):
    st.header("🔍 Buscar Libro", divider="rainbow")
    
    criterio = st.selectbox("Buscar por:", ["Título", "Autor", "ISBN", "Género"])
    valor = st.text_input(f"Introduzca el {criterio.lower()} a buscar")
    
    if st.button("Buscar", use_container_width=True):
        if valor:
            resultados = biblioteca.buscar_libro(criterio.lower(), valor)
            if resultados:
                st.success(f"📚 {len(resultados)} libros encontrados")
                for libro in resultados:
                    with st.expander(f"{libro.titulo} - {libro.autor}"):
                        st.markdown(libro.info_completa())
            else:
                st.warning("No se encontraron libros con esos criterios")
        else:
            st.warning("Introduzca un término de búsqueda")

def pagina_importar(biblioteca):
    st.header("📥 Importar Libros", divider="rainbow")
    
    st.info("""
        Puede importar libros desde un archivo CSV. El archivo debe contener al menos las columnas:
        - **Title**: Título del libro
        - **Author**: Autor del libro
        
        Columnas opcionales:
        - **ISBN**: Identificador del libro (10 o 13 dígitos)
        - **Genre**: Género literario
        - **Year**: Año de publicación
    """)
    
    archivo = st.file_uploader("Seleccione archivo CSV", type=["csv"])
    
    if archivo:
        contenido = archivo.getvalue().decode("utf-8")
        df = pd.read_csv(StringIO(contenido))
        
        st.subheader("Vista previa del archivo")
        st.dataframe(df.head(), use_container_width=True)
        
        if st.button("Importar Libros", use_container_width=True):
            with st.spinner("Procesando archivo..."):
                exito, mensaje = biblioteca.cargar_csv(contenido)
                if exito:
                    st.success(mensaje)
                else:
                    st.error(mensaje)

def pagina_historial(biblioteca):
    st.header("📜 Historial de Actividades", divider="rainbow")
    
    if not biblioteca.historial:
        st.info("No hay actividades registradas")
    else:
        df = pd.DataFrame(biblioteca.historial)
        st.dataframe(
            df.sort_values("fecha", ascending=False),
            use_container_width=True,
            column_config={
                "fecha": "Fecha/Hora",
                "accion": "Acción",
                "detalle": "Detalle"
            },
            hide_index=True
        )

def main():
    configurar_app()
    biblioteca = inicializar_biblioteca()
    
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=100)
        st.title("Biblioteca Digital")
        st.divider()
        
        pagina = st.radio(
            "Menú Principal",
            ["Inicio", "Agregar Libros", "Préstamos", "Buscar Libros", "Importar CSV", "Historial"],
            index=0
        )
        
        st.divider()
        st.markdown(f"""
            <div style="text-align: center;">
                <p>📚 <strong>Total libros:</strong> {len(biblioteca.libros)}</p>
                <p>✅ <strong>Disponibles:</strong> {sum(1 for l in biblioteca.libros.values() if l.disponible)}</p>
                <p>⏳ <strong>Prestados:</strong> {sum(1 for l in biblioteca.libros.values() if not l.disponible)}</p>
            </div>
        """, unsafe_allow_html=True)
    
    if pagina == "Inicio":
        pagina_inicio(biblioteca)
    elif pagina == "Agregar Libros":
        pagina_agregar(biblioteca)
    elif pagina == "Préstamos":
        pagina_prestamos(biblioteca)
    elif pagina == "Buscar Libros":
        pagina_buscar(biblioteca)
    elif pagina == "Importar CSV":
        pagina_importar(biblioteca)
    elif pagina == "Historial":
        pagina_historial(biblioteca)

if __name__ == "__main__":
    main()