class Persona:

    def __init__(self, nombre, apellido, sexo, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    def mostrar(self):
        print(f'Nombre: {self._nombre}, Apellido: {self.apellido}, Edad: {self.edad}')

class Empleado(Persona):

    def __init__(self, nombre, apellido, sexo, edad, codigo, sueldo):
        super().__init__(nombre, apellido, sexo, edad)
        self.codigo = codigo
        self.sueldo = sueldo

    def mostrar(self):
        print(f'Nombre: {self._nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Sueldo: {self.sueldo}')


persona = Persona('Ronaldo', 'Rodriguez', 'M', 26)
print(persona.nombre)
persona.nombre = 'Ricardo'
persona.mostrar()


emplead = Empleado('Ronaldo', 'Rodriguez', 'M', 26, 125, 1000)
print(emplead.nombre)
emplead.mostrar()