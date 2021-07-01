sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)
'''Escribir un programa que le permita al usuario adivinar un numero entre 1 y 9, 
si el usuario no adivina el numero imprimir "sigue intentando", de lo contrario debe terminar su ejecución'''