import time

for i in range(10,3):
    print ("el valor de i es = ",i)

#range(desde donde quiere comenzar, n-1 donde termina, saltos en el conteo)

# Ejemplo 1
palabra = "Python"
for letter in palabra:
    print(letter, end = "*")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end= "")

# ejemplo 2
for i in range(1, 11):
    print(i)
    time.sleep(1)

#ejemplo 3
lista = [23, 34, 54, 32, 51, 92]
suma = 0
for i in lista:
    suma += i

print(suma/len(lista)) 