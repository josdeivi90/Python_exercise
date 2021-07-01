#codigo para leer el tamaño de la lista
tamañoLista = int(input())
lista = []
#for para crear la lista
for i in range(0, tamañoLista):
    ele = int(input())
    lista.append(ele) # se añade el elemento
numeroMayor = lista[0]
numeroMenor = lista[0]
repetidos = []
#escribe tu codigo acá
#########
numeroMayor = max(lista)
numeroMenor = min(lista)

for i in lista:
    if (lista.count(i)>1 and i not in repetidos):
        repetidos.append(i)
    else:
        continue



##########
print(numeroMayor)
print(numeroMenor)
print(repetidos)
