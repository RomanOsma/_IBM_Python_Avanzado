print('*** Revision Valor Positivo ***')
numero = int(input('Proporciona un número: '))

if numero > 0:
    print(f'Es positivo: {numero}')
elif numero < 0:
    print(f'Es negativo: {numero}')
else:
    print(f'Es cero {numero}')
    
    
------
diagrama uml de actividad (flujo)
https://diagrams.helpful.dev/s/s:xpgncpvA

@startuml
!theme blueprint
start
:Revision Valor Positivo;
:Entrada: 'Proporciona un número:';

if (numero > 0) then (yes)
  :'Es positivo';
elseif (numero < 0) then (no)
  :'Es negativo';
else (Cero)
  :'Es cero';
endif

stop
@enduml

https://diagrams.helpful.dev/s/s:m43Fbp9O
