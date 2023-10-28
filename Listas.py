paises = ['Venezuela', 'Colombia', 'Argentina', 'USA']

print(paises)
print(paises[:1])

paises[2] = 'Mexico'

print(paises)

for pais in paises:
    print(pais)
else:
    print("Ya no existen mas")

print(len(paises))

paises.append('China')
paises.insert(1, 'Chile')

print(paises)