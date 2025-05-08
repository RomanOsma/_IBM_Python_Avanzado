from empleado import Empleado
from empresa import Empresa

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Mi Empresa')

# Contratar algunos empleados
empresa1.contrar_empleado('Juan', 'Ventas')
empresa1.contrar_empleado('María', 'Marketing')
empresa1.contrar_empleado('Pedro', 'Ventas')
empresa1.contrar_empleado('Ana', 'Recursos Humanos')

# Obtener el numero total de empleados de la empresa creada
print(f'Total de empleados en la empresa: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de Ventas
print(f'Empleados en el departamento de Ventas: '
      f'{empresa1.obtener_numero_empleados_departamento('Ventas')}')
