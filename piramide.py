bloques = int(input("Ingrese el número de bloques par: "))

altura = 0
while(bloques > 0 ):
    altura += 1
    bloques -= altura


print("La altura de la pirámide:", altura)
