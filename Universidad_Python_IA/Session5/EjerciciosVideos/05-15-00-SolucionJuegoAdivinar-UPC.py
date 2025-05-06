from random import randint

print('*** Juego de Adivinanzas ***')

numero_secreto = randint(1, 50)
intentos = 0
INTENTOS_MAXIMOS = 5
adivinanza = None

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el número secreto (entre 1 y 50): '))
    intentos += 1
    # Agregamos una ayuda para orientar al usuario, y sepa si el numero proporcionado fue mayor o menor
    # que el numero secreto
    if adivinanza < numero_secreto:
        print('El número secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El número secreto es menor')
# Concluimos el juego
if adivinanza == numero_secreto:
    print(f'Felicidades, adivinaste el número secreto en {intentos} intentos')
else:
    print(f'Lo siento, has agotado tus intentos maximos: {INTENTOS_MAXIMOS}')
    print(f'El número secreto era: {numero_secreto}')