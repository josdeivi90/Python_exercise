numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprime el contenido de la lista original

numeros[0] = 111  # asigno a la posicion 0 el valor 111
print("Nuevo contenido de la lista:", numeros) # contenido de la lista actual.

numeros[4] = 1113  # asigno a la posicion 0 el valor 111
print("Nuevo contenido de la lista:", numeros) # contenido de la lista actual.

numeros[1] = numeros[4]  # asigno a la posicion 0 el valor 111
print("Nuevo contenido de la lista:", numeros) # contenido de la lista actual.

print(numeros[-2])