numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)

miLista = [] # creando una lista vacía
miLista2 = [1,2,4,5,3]
for i in range (5):
    miLista.append (i + 1)
    miLista2.insert(3,i+20)
print(miLista)
print(miLista2)