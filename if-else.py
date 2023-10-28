variable = 5
otraVariable = 10

if variable < otraVariable:
    print('Verdadero')
else:
    print('Falso')

numero = int(input('Indica un numero del 1 al 3:'))
mensaje = ''

if numero == 1:
    mensaje = 'Indico el numero 1'
elif numero == 2:
    mensaje = 'Indico el numero 2'
elif numero == 3:
    mensaje = 'Indico el numero 3'
else:
    mensaje = 'No indico un numero valido'

print(f"El mensaje que selecciono es: {mensaje}")


condicion = False

print('Verdadero') if condicion else print('Falso')

