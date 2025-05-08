import zipfile

# Paths
zip_path = 'temario.zip'
output_py = 'Guia_Tkinter_Completo.py'
output_pdf = 'Guia_Tkinter_Completo.pdf'

# Extract and unify code
with zipfile.ZipFile(zip_path, 'r') as z:
    # Filter python files excluding __pycache__
    py_files = [f for f in z.namelist() if f.endswith('.py') and '__pycache__' not in f]
    with open(output_py, 'w', encoding='utf-8') as out_py:
        out_py.write('"""\nGuía Completa de Tkinter - Código Unificado\n"""\n\n')
        for file in sorted(py_files):
            out_py.write(f'# ======= {file} ========\n')
            with z.open(file) as f:
                content = f.read().decode('utf-8', errors='ignore')
                # Write content with indentation guard
                out_py.write(content + '\n\n')

# Generate a simple PDF listing sections
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
c = canvas.Canvas(output_pdf, pagesize=letter)
width, height = letter
y = height - 40
c.setFont("Helvetica-Bold", 14)
c.drawString(40, y, "Guía Completa de Tkinter - Contenido de Código")
c.setFont("Helvetica", 10)
y -= 30
for file in sorted(py_files):
    if y < 40:
        c.showPage()
        y = height - 40
        c.setFont("Helvetica", 10)
    c.drawString(50, y, f"- {file}")
    y -= 12
c.save()

print("Archivos completos generados:")
print(f" - Código unificado: {output_py}")
print(f" - PDF con índice de código: {output_pdf}")
