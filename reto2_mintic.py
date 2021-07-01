'''Una compañia de electricidad cobra a los usuarios de la siguiente manera

Las primeras 50 unidades de energia se cobra a  450 pesos el total de unidades
Las siguientes 100 unidades de energia se cobra a  500 pesos el total de unidades
Las siguientes 100 unidades de energia se cobra a  650 pesos el total de unidades
En adelante el costo es 800 el total de unidades

Despues de hallar el calcular el costo total se agrega un 20% al valor de la factura

Escribe un programa que permita al usuario ingresar el numero de unidades consumidas y me devuelva el valor
 total a pagar de la factura.

Planteamiento del reto

Con respecto a la situación planteada, ¿De qué manera crees que María Fernanda puede automatizar valor total
de la factura de electricidad?.
Acciones de aprendizaje

a. Analizar, identificar y declarar las variables que considere necesarias para realizar los
 cálculos de costo por unidad basado en la cantidad de unidades consumida.
b. Determinar desde las variables identificadas, cual(es) corresponden a los datos de entrada, 
las operaciones entre ellas que dan solución al reto, y cual(es) son los datos para presentar como salida.
c. Diseñar el algoritmo en lenguaje python.

Escriba el algoritmo diseñado para solucionar el reto.

Tenga en cuenta que si el usuario ingresa un valor negativo de unidades el programa debe responder "Valor incorrecto"
Entrada	Resultado
150       90000.0


'''
import time
while True:
    energia = float(input("Ingrese un valor numerico correspondiente a las unidades consumidas = "))

    unidades = 0
    factura = 0

    if(0<energia<=50):
        factura = (energia*450)+(energia*450*0.2)
    elif(51<=energia<=151):
        factura = (energia*500)+(energia*500*0.2)
    elif(152<=energia<=252):
        factura = (energia*650)+(energia*650*0.2)
    elif(energia>252):
        factura = (energia*800)+(energia*800*0.2)
    else:
        print("Valor incorrecto")
    print("El valor de la factura es = ",factura)
    time.sleep(3)