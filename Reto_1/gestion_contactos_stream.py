import re
import os
import streamlit as st
from datetime import datetime
from typing import List, Optional

class Contacto:
    def __init__(self, nombre: str, telefono: str, correo: str, empresa: str = "", categoria: str = "Personal"):
        """
        Clase que representa un contacto en la agenda.
        
        Args:
            nombre (str): Nombre completo del contacto
            telefono (str): Número de teléfono
            correo (str): Dirección de correo electrónico
            empresa (str, optional): Empresa del contacto. Defaults to "".
            categoria (str, optional): Categoría del contacto (Personal, Trabajo, Familia). Defaults to "Personal".
        """
        self.nombre = nombre.strip()
        self.telefono = telefono.strip()
        self.correo = correo.strip()
        self.empresa = empresa.strip()
        self.categoria = categoria.strip()
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.fecha_actualizacion = self.fecha_creacion

    def actualizar(self, **kwargs):
        """Actualiza los campos del contacto"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value.strip() if isinstance(value, str) else value)
        self.fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self) -> dict:
        """Convierte el contacto a un diccionario"""
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "empresa": self.empresa,
            "categoria": self.categoria,
            "fecha_creacion": self.fecha_creacion,
            "fecha_actualizacion": self.fecha_actualizacion
        }

    def __str__(self) -> str:
        return f"{self.nombre} | {self.telefono} | {self.correo}"

class GestionContactos:
    def __init__(self, archivo: str = 'contactos.csv'):
        """
        Clase para gestionar una lista de contactos con persistencia en archivo.
        
        Args:
            archivo (str, optional): Nombre del archivo de almacenamiento. Defaults to 'contactos.csv'.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.archivo = os.path.join(script_dir, archivo)
        self.contactos: List[Contacto] = []
        self.cargar_contactos()

    @staticmethod
    def validar_correo(correo: str) -> bool:
        """Valida el formato de un correo electrónico"""
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(patron, correo)) if correo else False

    @staticmethod
    def validar_telefono(telefono: str) -> bool:
        """Valida que el teléfono contenga solo dígitos y tenga longitud adecuada"""
        return telefono.isdigit() and 7 <= len(telefono) <= 15

    def cargar_contactos(self):
        """Carga los contactos desde el archivo CSV"""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    next(f)  # Saltar encabezados
                    for linea in f:
                        datos = linea.strip().split(',')
                        if len(datos) >= 3:
                            contacto = Contacto(
                                nombre=datos[0],
                                telefono=datos[1],
                                correo=datos[2],
                                empresa=datos[3] if len(datos) > 3 else "",
                                categoria=datos[4] if len(datos) > 4 else "Personal"
                            )
                            if len(datos) > 5:
                                contacto.fecha_creacion = datos[5]
                            if len(datos) > 6:
                                contacto.fecha_actualizacion = datos[6]
                            self.contactos.append(contacto)
        except Exception as e:
            st.error(f"Error al cargar contactos: {e}")

    def guardar_contactos(self):
        """Guarda los contactos en un archivo CSV"""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                f.write("Nombre,Telefono,Correo,Empresa,Categoria,Fecha Creacion,Fecha Actualizacion\n")
                for contacto in self.contactos:
                    datos = [
                        contacto.nombre,
                        contacto.telefono,
                        contacto.correo,
                        contacto.empresa,
                        contacto.categoria,
                        contacto.fecha_creacion,
                        contacto.fecha_actualizacion
                    ]
                    f.write(','.join(datos) + '\n')
        except Exception as e:
            st.error(f"Error al guardar contactos: {e}")

    def agregar_contacto(self, contacto: Contacto) -> bool:
        """Agrega un nuevo contacto a la lista"""
        if not self.validar_correo(contacto.correo):
            st.error("Formato de correo electrónico inválido")
            return False
        if not self.validar_telefono(contacto.telefono):
            st.error("Teléfono debe contener solo dígitos (7-15 caracteres)")
            return False
        
        self.contactos.append(contacto)
        self.guardar_contactos()
        return True

    def buscar_contactos(self, criterio: str, valor: str) -> List[Contacto]:
        """Busca contactos por un criterio específico"""
        valor = valor.lower()
        if criterio == "nombre":
            return [c for c in self.contactos if valor in c.nombre.lower()]
        elif criterio == "telefono":
            return [c for c in self.contactos if valor in c.telefono]
        elif criterio == "correo":
            return [c for c in self.contactos if valor in c.correo.lower()]
        elif criterio == "empresa":
            return [c for c in self.contactos if valor in c.empresa.lower()]
        elif criterio == "categoria":
            return [c for c in self.contactos if c.categoria.lower() == valor]
        return []

    def eliminar_contacto(self, correo: str) -> bool:
        """Elimina un contacto por su correo electrónico"""
        for i, contacto in enumerate(self.contactos):
            if contacto.correo.lower() == correo.lower():
                del self.contactos[i]
                self.guardar_contactos()
                return True
        return False

    def actualizar_contacto(self, correo_original: str, **kwargs) -> bool:
        """Actualiza los datos de un contacto existente"""
        for contacto in self.contactos:
            if contacto.correo.lower() == correo_original.lower():
                contacto.actualizar(**kwargs)
                self.guardar_contactos()
                return True
        return False

    def obtener_categorias(self) -> List[str]:
        """Obtiene la lista de categorías únicas"""
        categorias = set(c.categoria for c in self.contactos)
        return sorted(categorias) if categorias else ["Personal"]

# Configuración de la aplicación
def configurar_app():
    st.set_page_config(
        page_title="Gestión de Contactos",
        page_icon="📇",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.markdown("""
        <style>
            .st-emotion-cache-1kyxreq {justify-content: center;}
            .contact-card {border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px 0;}
            .contact-card h3 {margin-top: 0;}
            .header {color: #2e86c1;}
        </style>
    """, unsafe_allow_html=True)

def mostrar_contacto(contacto: Contacto):
    """Muestra una tarjeta visual para un contacto"""
    st.markdown(f"""
        <div class="contact-card">
            <h3>{contacto.nombre}</h3>
            <p><strong>📞 Teléfono:</strong> {contacto.telefono}</p>
            <p><strong>✉️ Correo:</strong> {contacto.correo}</p>
            <p><strong>🏢 Empresa:</strong> {contacto.empresa or 'No especificada'}</p>
            <p><strong>🏷️ Categoría:</strong> {contacto.categoria}</p>
            <p><small>Creado: {contacto.fecha_creacion} | Actualizado: {contacto.fecha_actualizacion}</small></p>
        </div>
    """, unsafe_allow_html=True)

def pagina_inicio(gestion: GestionContactos):
    st.header("📇 Todos los Contactos", divider="rainbow")
    
    col1, col2 = st.columns(2)
    with col1:
        filtro_categoria = st.selectbox(
            "Filtrar por categoría",
            ["Todas"] + gestion.obtener_categorias()
        )
    with col2:
        buscar = st.text_input("Buscar contactos")
    
    contactos_filtrados = gestion.contactos
    
    if filtro_categoria != "Todas":
        contactos_filtrados = [c for c in contactos_filtrados if c.categoria == filtro_categoria]
    
    if buscar:
        contactos_filtrados = [
            c for c in contactos_filtrados 
            if buscar.lower() in c.nombre.lower() 
            or buscar.lower() in c.correo.lower()
            or buscar in c.telefono
        ]
    
    if not contactos_filtrados:
        st.info("No hay contactos que coincidan con los criterios de búsqueda")
    else:
        for contacto in sorted(contactos_filtrados, key=lambda x: x.nombre):
            mostrar_contacto(contacto)
    
    st.metric("Total de contactos", len(gestion.contactos))

def pagina_agregar(gestion: GestionContactos):
    st.header("➕ Agregar Nuevo Contacto", divider="rainbow")
    
    with st.form("form_agregar", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre completo*")
            telefono = st.text_input("Teléfono*", help="Solo números, 7-15 dígitos")
        with col2:
            correo = st.text_input("Correo electrónico*")
            empresa = st.text_input("Empresa")
        
        categoria = st.selectbox(
            "Categoría",
            gestion.obtener_categorias() + ["Nueva categoría..."]
        )
        
        if categoria == "Nueva categoría...":
            categoria = st.text_input("Ingrese la nueva categoría")
        
        if st.form_submit_button("Guardar Contacto", use_container_width=True):
            if not nombre or not telefono or not correo:
                st.error("Los campos marcados con * son obligatorios")
            else:
                contacto = Contacto(
                    nombre=nombre,
                    telefono=telefono,
                    correo=correo,
                    empresa=empresa,
                    categoria=categoria
                )
                if gestion.agregar_contacto(contacto):
                    st.success("Contacto agregado correctamente")
                    st.balloons()

def pagina_buscar(gestion: GestionContactos):
    st.header("🔍 Buscar Contactos", divider="rainbow")
    
    criterio = st.selectbox("Buscar por", ["nombre", "telefono", "correo", "empresa", "categoria"])
    valor = st.text_input(f"Introduzca el {criterio} a buscar")
    
    if st.button("Buscar", use_container_width=True):
        if valor:
            resultados = gestion.buscar_contactos(criterio, valor)
            if resultados:
                st.success(f"📇 {len(resultados)} contactos encontrados")
                for contacto in resultados:
                    with st.expander(f"{contacto.nombre} - {contacto.correo}"):
                        mostrar_contacto(contacto)
                        
                        # Opciones de edición y eliminación
                        with st.form(f"editar_{contacto.correo}"):
                            st.write("**Editar contacto**")
                            nuevo_nombre = st.text_input("Nombre", contacto.nombre)
                            nuevo_telefono = st.text_input("Teléfono", contacto.telefono)
                            nuevo_correo = st.text_input("Correo", contacto.correo)
                            nueva_empresa = st.text_input("Empresa", contacto.empresa)
                            nueva_categoria = st.text_input("Categoría", contacto.categoria)
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                if st.form_submit_button("Actualizar"):
                                    gestion.actualizar_contacto(
                                        contacto.correo,
                                        nombre=nuevo_nombre,
                                        telefono=nuevo_telefono,
                                        correo=nuevo_correo,
                                        empresa=nueva_empresa,
                                        categoria=nueva_categoria
                                    )
                                    st.rerun()
                            with col2:
                                if st.form_submit_button("Eliminar"):
                                    gestion.eliminar_contacto(contacto.correo)
                                    st.rerun()
            else:
                st.warning("No se encontraron contactos con esos criterios")
        else:
            st.warning("Introduzca un término de búsqueda")

def main():
    configurar_app()
    gestion = GestionContactos()
    
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1077/1077063.png", width=80)
        st.title("Gestión de Contactos")
        st.divider()
        
        pagina = st.radio(
            "Menú Principal",
            ["Inicio", "Agregar Contacto", "Buscar Contactos"],
            index=0
        )
        
        st.divider()
        st.markdown(f"""
            <div style="text-align: center;">
                <p>📇 <strong>Total contactos:</strong> {len(gestion.contactos)}</p>
                <p>🏷️ <strong>Categorías:</strong> {len(gestion.obtener_categorias())}</p>
            </div>
        """, unsafe_allow_html=True)
    
    if pagina == "Inicio":
        pagina_inicio(gestion)
    elif pagina == "Agregar Contacto":
        pagina_agregar(gestion)
    elif pagina == "Buscar Contactos":
        pagina_buscar(gestion)

if __name__ == "__main__":
    main()