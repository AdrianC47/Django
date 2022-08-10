#clases
class Persona():
    nombre = ''
    apellidos = ''
    edad = 0

    def __init__(self): # esto es un constructor, el cual de igual manera lleva como parametro el self
        self.edad=22
        self.nombre= 'Adrian'
#las clases pueden tener funciones
#Siempre las funciones que pertenecen a una clase deben llevar como atributo el self
    def full_name(self):
        return self.nombre + '-' + self.apellidos + ' '+ str(self.edad) ## retornamos el self para poder acceder a los atributos de la clase

persona = Persona()
print(persona.edad)
persona.apellidos='Cabrera'
print(persona.full_name())
