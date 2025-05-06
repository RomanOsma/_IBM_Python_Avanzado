print('*** Sistema Prestamo de Libros ***')

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('Cuentas con credencial de estudiante (Si/No)? ')
distancia_biblioteca_km = int(input('A cuantos km vives de la biblioteca? '))

es_elegible_prestamo = (tiene_credencial.lower() == 'si'
                        or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f'Eres elegible para prestamo de libros? {es_elegible_prestamo}')