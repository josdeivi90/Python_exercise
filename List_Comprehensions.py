i = int(input("corrdenada X = "))
j = int(input("corrdenada Y = "))
k = int(input("corrdenada Z = "))
n = int(input("corrdenada n = "))

lista = [[x, y, z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if x+y+z!=n]



print (lista)

