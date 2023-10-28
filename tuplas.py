colores = ('Amarillo', 'Rojo', 'Azul', 'Blanco')

print(colores)
print(len(colores))
print(colores[-1])

for color in colores:
    print(color, end=', ')

coloresLista = list(colores)
coloresLista[1] = 'Gris'

colores = tuple(coloresLista)

print(colores)



