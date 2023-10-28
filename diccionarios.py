diccionario = {
    'nombre': 'Ronaldo',
    'apellido': 'Rodriguez'
}

print(diccionario)
print(diccionario['nombre'])
# print(diccionario.get('nombre'))

diccionario['nombre'] = 'Juan'
print(diccionario['nombre'])

for key, value in diccionario.items():
    print(key, value)

for key in diccionario.keys():
    print(key)
    
for value in diccionario.values():
    print(value)