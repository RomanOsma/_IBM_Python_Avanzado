import zipfile
import os  # Necesario para manipular rutas de archivo
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# --- Configuración de Nombres de Archivo ---
# Cambia 'temario_flask.zip' si tu archivo ZIP se llama diferente.
zip_path = 'temario.zip'  # El usuario debe asegurarse de que este archivo exista
output_py = 'Guia_Flask_Completa_Unificada.py'
output_pdf = 'Guia_Flask_Completa_Indice.pdf'


# --- Función para Formatear Nombres de Archivo para Visualización ---
def formatear_nombre_display(ruta_en_zip):
    """
    Crea un nombre más legible a partir de la ruta completa del archivo en el ZIP.
    Ejemplo: "Leccion01-HolaFlask/ManejoFlask/app.py" -> "Leccion01-HolaFlask - app.py"
    """
    # Los archivos ZIP usan '/' como separador universalmente.
    partes = ruta_en_zip.split('/')

    nombre_archivo_original = partes[-1]  # El nombre del archivo en sí, ej: "app.py"

    if len(partes) == 1:
        # El archivo está en la raíz del ZIP, no hay ruta que simplificar.
        return nombre_archivo_original

    # El primer elemento de la ruta suele ser el nombre de la lección o módulo.
    nombre_leccion_bruto = partes[0]

    # Limpiar sufijos comunes como "(1)", "(copia)", etc., del nombre de la lección.
    nombre_leccion_limpio = nombre_leccion_bruto
    for i in range(1, 10):  # Quita " (1)" hasta " (9)"
        nombre_leccion_limpio = nombre_leccion_limpio.replace(f" ({i})", "")
    # Puedes añadir más reemplazos si es necesario:
    # nombre_leccion_limpio = nombre_leccion_limpio.replace("-UPC", "") # Ejemplo

    # Lista de nombres de carpetas comunes en proyectos que podríamos querer omitir del nombre final
    # si están justo antes del nombre del archivo, para no ser redundantes.
    carpetas_proyecto_comunes = ["manejoflask", "flask_app", "src", "source", "proyecto_flask", "app"]

    if len(partes) > 2 and partes[-2].lower() in carpetas_proyecto_comunes:
        # Estructura tipo: "NOMBRE_LECCION/CARPETA_PROYECTO_COMUN/nombre_archivo.py"
        # Resultado: "NOMBRE_LECCION - nombre_archivo.py"
        nombre_display = f"{nombre_leccion_limpio} - {nombre_archivo_original}"
    elif len(partes) > 1:
        # Estructura tipo: "NOMBRE_LECCION/nombre_archivo.py" o "NOMBRE_LECCION/SUBTEMA/nombre_archivo.py"
        sub_camino_intermedio = " - ".join(partes[1:-1])  # Recoge carpetas intermedias
        if sub_camino_intermedio:
            nombre_display = f"{nombre_leccion_limpio} - {sub_camino_intermedio} - {nombre_archivo_original}"
        else:  # Solo "NOMBRE_LECCION/nombre_archivo.py"
            nombre_display = f"{nombre_leccion_limpio} - {nombre_archivo_original}"
    else:
        # Caso por defecto, aunque los anteriores deberían cubrirlo.
        nombre_display = nombre_archivo_original

    return nombre_display.replace('/', '_')  # Asegura que no queden barras


# --- Procesamiento Principal ---
try:
    with zipfile.ZipFile(zip_path, 'r') as z:
        py_files_info = []  # Almacenará diccionarios con {'original': ruta_zip, 'display': nombre_formateado}

        lista_archivos_zip = z.namelist()
        for ruta_original_en_zip in lista_archivos_zip:
            # Filtrar solo archivos .py, excluyendo carpetas de caché y metadatos de Mac.
            if ruta_original_en_zip.endswith('.py') and \
                    '__pycache__' not in ruta_original_en_zip and \
                    not ruta_original_en_zip.startswith('__MACOSX/'):
                nombre_formateado = formatear_nombre_display(ruta_original_en_zip)
                py_files_info.append({'original': ruta_original_en_zip, 'display': nombre_formateado})

        # Ordenar los archivos (opcional, pero bueno para consistencia).
        # Se ordena por la ruta original para mantener el orden del curso si es secuencial.
        py_files_info.sort(key=lambda x: x['original'])

        # 1. Crear el archivo .py unificado
        with open(output_py, 'w', encoding='utf-8') as out_py:
            out_py.write(f'"""\nGuía Completa de Flask - Código Unificado del Curso\n"""\n\n')
            for info in py_files_info:
                # Usar el nombre formateado en el comentario para legibilidad.
                out_py.write(f'# {"=" * 10} Inicio de: {info["display"]} {"=" * 10}\n')
                out_py.write(f'# (Archivo original en ZIP: {info["original"]})\n')
                try:
                    with z.open(info['original']) as f_content:
                        contenido_script = f_content.read().decode('utf-8', errors='ignore')
                        out_py.write(contenido_script + '\n\n')
                except Exception as e_open:
                    out_py.write(f"# ERROR al leer el archivo {info['original']}: {e_open}\n\n")
            out_py.write(f'# {"=" * 10} Fin de la Guía Completa de Flask {"=" * 10}\n')

        # 2. Generar el PDF con el índice usando los nombres formateados
        c = canvas.Canvas(output_pdf, pagesize=letter)
        width, height = letter  # Obtener dimensiones de la página

        y_position = height - 40  # Posición Y inicial (desde arriba)
        line_height_pdf = 12
        margin_bottom_pdf = 40

        c.setFont("Helvetica-Bold", 16)
        c.drawString(40, y_position, "Guía Completa de Flask - Índice del Código")
        y_position -= (line_height_pdf * 2)  # Espacio después del título

        c.setFont("Helvetica", 10)
        for info in py_files_info:
            if y_position < margin_bottom_pdf:  # Si no hay espacio, nueva página
                c.showPage()
                y_position = height - margin_bottom_pdf  # Reiniciar Y
                c.setFont("Helvetica-Bold", 12)  # Título de continuación
                c.drawString(40, y_position, "Índice del Código (Continuación)")
                y_position -= (line_height_pdf * 2)
                c.setFont("Helvetica", 10)

            # Dibujar el nombre formateado en el PDF
            c.drawString(50, y_position, f"- {info['display']}")
            y_position -= line_height_pdf

        c.save()

        print("¡Proceso completado exitosamente!")
        print(f"  -> Código Python unificado generado en: {output_py}")
        print(f"  -> Índice PDF generado en: {output_pdf}")

except FileNotFoundError:
    print(f"Error: El archivo ZIP '{zip_path}' no fue encontrado.")
    print("Por favor, asegúrate de que el archivo esté en la misma carpeta que este script,")
    print("o modifica la variable 'zip_path' con la ruta correcta.")
except Exception as e:
    print(f"Ocurrió un error inesperado durante el proceso: {e}")