# ==============================================================================
# CLASE: Operadores en Python
# ==============================================================================

# Los operadores en Python se utilizan para realizar operaciones sobre variables y valores.

# ----------------------------------------------------
# 42. Operadores Aritméticos
# ----------------------------------------------------
a = 10
b = 3

# Suma
print("Suma:", a + b)

# Resta
print("Resta:", a - b)

# Multiplicación
print("Multiplicación:", a * b)

# División
print("División:", a / b)  # Devuelve un float

# División entera
print("División entera:", a // b)  # Devuelve la parte entera

# Módulo (residuo)
print("Módulo:", a % b)

# Potenciación
print("Potencia:", a ** b)

# ----------------------------------------------------
# 43. Operadores de Asignación
# ----------------------------------------------------
x = 5  # Asignación simple
x += 3  # Suma y asigna (x = x + 3)
x -= 2  # Resta y asigna
x *= 2  # Multiplica y asigna
x /= 3  # Divide y asigna
x %= 4  # Módulo y asigna
x **= 2  # Potencia y asigna
x //= 2  # División entera y asigna

print("Resultado final de x:", x)

# ----------------------------------------------------
# 45. Operadores de Comparación
# ----------------------------------------------------
a = 10
b = 20

print("a == b:", a == b)  # Igualdad
print("a != b:", a != b)  # Diferente
print("a > b:", a > b)    # Mayor que
print("a < b:", a < b)    # Menor que
print("a >= b:", a >= b)  # Mayor o igual
print("a <= b:", a <= b)  # Menor o igual

# ----------------------------------------------------
# 46. Operador Lógico and
# ----------------------------------------------------
usuario_vip = True
compra_mayor_100 = True

if usuario_vip and compra_mayor_100:
    print("Descuento aplicado")

# ----------------------------------------------------
# 47. Ejercicio - Sistema de Descuentos VIP
# ----------------------------------------------------
# Entrada: ¿Es VIP? ¿Compra mayor a 100?
# Salida: Aplicar descuento solo si ambas condiciones son verdaderas.

vip = True
monto_compra = 120

if vip and monto_compra > 100:
    print("Aplica descuento del 20%")
else:
    print("No aplica descuento")

# ----------------------------------------------------
# 48. Operador Lógico or
# ----------------------------------------------------
tiene_carnet = False
es_estudiante = True

if tiene_carnet or es_estudiante:
    print("Puede tomar libros prestados")

# ----------------------------------------------------
# 49. Ejercicio - Préstamo de Libros
# ----------------------------------------------------
# Permitir préstamo si tiene carnet o si es estudiante

carnet = False
estudiante = False

if carnet or estudiante:
    print("Préstamo autorizado")
else:
    print("Acceso denegado")
# ----------------------------------------------------
print('*** Sistema Prestamo de Libros ***')

DISTANCIA_PERMITIDA_KM = 5
credencial = input('Cuentas con credencial de estudiante (Si/No)? ')
distancia_biblioteca_km = int(input('A cuantos km vives de la biblioteca? '))

es_elegible_prestamo = (credencial.lower() == 'si'
                        or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f'Eres elegible para prestamo de libros? {es_elegible_prestamo}')

# ----------------------------------------------------
# 50. Operador Lógico not
# ----------------------------------------------------
activo = False

if not activo:
    print("El usuario está inactivo")

# ----------------------------------------------------
# 51-52. Ejercicio Ticket de Venta (con y sin descuento)
# ----------------------------------------------------
producto = "Teclado"
precio = 100
descuento = 0.1  # 10% de descuento

# Aplicar descuento si precio mayor a 50
if precio > 50:
    precio_final = precio * (1 - descuento)
else:
    precio_final = precio

print("Producto:", producto)
print("Precio final:", precio_final)

# ----------------------------------------------------

# Ticket de Venta de una compra en un supermercado
print('*** Generacion Ticket de Venta ***')
precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio platanos: '))
descuento_porcentaje = int(input('Aplicar algún descuento(%)? '))

# Calcular el subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calcular el impuesto (21%)
impuesto = subtotal_con_descuento * .21

# Calculo total de la compra (incluyendo impuestos)
costo_total_compra = subtotal_con_descuento + impuesto

# Generar el ticket de venta
# .2f es el formato de saliada
print(f'''
--- Ticket de Venta ---
Subtotal: ${subtotal:.2f} 
Descuento: ${descuento} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento:.2f}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
''')

# ----------------------------------------------------
# 53-54. Sistema de Autenticación
# ----------------------------------------------------
usuario_esperado = "admin"
clave_esperada = "1234"

usuario_ingresado = input('Cual es tu usuario? ')
password_ingresado = input('Cual es tu password? ')
acceso = (usuario_ingresado == usuario_ingresado and password_ingresado == clave_esperada)

if acceso:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# ----------------------------------------------------
# 55. Precedencia de Operadores
# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)
# ----------------------------------------------------
# Resumen -> Paréntesis > Potencia > Multiplicación/División > Suma/Resta
resultado = 3 + 2 * 2  # Resultado = 7
resultado2 = (3 + 2) * 2  # Resultado = 10
resultado3 = 12 / 3 + 2 * 3 - 1
resultado4 = 12 / (3 + 2) * 3 - 1
print(f'Resultado: {resultado}')
print(f'Resultado: {resultado2}')
print("Resultado 2:", resultado3)
print("Resultado 2:", resultado4)
# ----------------------------------------------------
# 56-57. Ejercicio - Valor dentro de Rango
# ----------------------------------------------------
numero = 15
rango_min = 10
rango_max = 20

# if rango_min <= numero <= rango_max:
if numero >= rango_min and numero <= rango_max:
    print("Número dentro de rango")
else:
    print("Número fuera de rango")

# ----------------------------------------------------
# 58-59. Área de un Rectángulo
# ----------------------------------------------------
# Fórmula: área = base * altura
base = 5
altura = 10

area = base * altura
perimetro = 2 *(base + altura)
print("Área del rectángulo:", area)
print("Perimetro del rectángulo:", perimetro)
