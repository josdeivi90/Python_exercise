fila = []

for i in range(8):
    fila.append("PEON_BLANCO")

fila2 = ["PEON_BLANCO" for i in range(3)] #forma de recortar la lista

cuadrados = [x ** 2 for x in range(10)] #imprime los cuadrados hasta 10
print(cuadrados)

dos = [2 ** i for i in range(8)] #El fragmento crea un arreglo de ocho elemento
#s que contiene las primeras ocho potencias del numero dos (1, 2, 4, 8, 16, 32, 64, 128)
print(dos)

probabilidades = [x for x in cuadrados if x % 2 != 0] 
#El fragmento hace una lista con solo los elementos impares de la lista
print(probabilidades)

temps = [[0.0 for h in range (24)] for d in range (31)] #PARA IMPRIMIR VALORES M*N
#print(temps)

habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)] #matrices para imagenes
print(habitaciones)
