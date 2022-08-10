# 5 Cadenas, listas, tuplas y diccionarios
texto = 'Cadena de prueba'
texto2= 'del curso  de python'
print(texto + ' ' +texto2)
print(texto[0])
print(len(texto))
# cadenas
# Listas
lista = ['manzanas', 'peras','naranjas', 10, 20, ['a', 'b','c']]
lista.append('Nuevo01')
lista.insert(0, 'elemento0')
lista.remove('manzanas')
lista.pop(2) #me sirve para de igual manera eliminar un elemento pero indicando su posicion
print(lista)
lista.clear()
lista.reverse()
# Diccionarios... tienen clave y valor
diccionario = {
    'id':10,
    'nombre': 'Adrian',
    'apellido': 'Cabrera'
}
print(diccionario)
print(diccionario['nombre'])
# bucles repetitivos
lista = ['manzanas', 'peras','naranjas', 10, 20, ['a', 'b','c']]
#imprimir un elemento de una lsita que esta dentro de otra lista
print((lista[5])[1])
# while
num1 = 0
while (num1 < len(lista)):
    print('elemento: ', lista[num1])
    num1 += 1

#for
for l in lista:
    print('elemento 2: ', l)

