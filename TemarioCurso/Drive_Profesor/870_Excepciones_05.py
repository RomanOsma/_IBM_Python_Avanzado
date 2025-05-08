# Crear tus propias excepciones

# La palabra clave raise lanza una excepción (es decir, provoca un error 
# intencionalmente) en el momento que tú decides, para que el flujo del 
# programa salte al bloque except correspondiente o se detenga si no se captura.

# ¿Por qué querrías lanzar una excepción tú mismo?
# Para validar datos (por ejemplo, edades negativas, textos vacíos, etc.).

# Para detectar condiciones anómalas en tu código y tratarlas de forma controlada.

# Para usar tus propias excepciones personalizadas.


class EdadInvalidaError(Exception):
    pass

def verificar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")
    print("Edad válida:", edad)

try:
    verificar_edad(-5)
except EdadInvalidaError as e:
    print("Error personalizado:", e)