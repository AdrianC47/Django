# funciones
# def simples
def saludar(saludo):
    print(saludo)

saludar('Hola como parametro')
# def con parametro por defecto
def saludar2(saludo='Hola como valor por defecto'):
    print(saludo)
saludar2()
saludar2('Hola como valor nuevo')
# def con parametro lista   ..se pone el asterisco
def saludar3(*lista):
    print(lista)

saludar3(['uno', 'dos', 'tres'])
# def con parametro diccionario .. en el caso de los diccionarios se pone doble asterisco

def saludar4(**lista):
    print(lista)

saludar4(diccionario = {
    'id':10,
    'nombre': 'Adrian',
    'apellido': 'Cabrera'
})
