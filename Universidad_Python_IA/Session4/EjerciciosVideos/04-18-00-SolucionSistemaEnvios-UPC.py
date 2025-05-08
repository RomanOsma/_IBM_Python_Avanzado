print('*** Sistema de Envíos ***')

# Definimos las tarifas de envío por kilogramo
TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitar los valores de destino y peso
destino = input('Ingresa el destino del paquete (nacional o internacional): ')
peso = float(input('Ingresa el peso del paquete (en kg): '))

costo_envio = None # Definimos la variable de costo de envio

# Calculo del costo de envío
if destino.lower() == 'nacional':
    costo_envio = peso * TARIFA_NACIONAL
elif destino.lower() == 'internacional':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print('Destino no válido. Ingresa el valor de nacional o internacional')

# Mostrar el costo de envío sólo si es un valor válido
if costo_envio is not None:
    print(f'El costo de envío del paquete es: ${costo_envio:.2f}')