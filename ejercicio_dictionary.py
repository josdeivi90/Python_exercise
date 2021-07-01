'''Write a Python program to split a given dictionary of lists into list of dictionaries. Go to the editor
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

lista = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1),("black",123),]
diccionario = {}
for i in lista:
    lista1 = diccionario.get(i[0],[])
    lista1.append(i[1])
    diccionario[i[0]] = lista1
print(diccionario)


'''

dict1 = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}



x1 = list(dict1.keys())
x2 = list(dict1.values())


l2 = len(x1) #longitud de las llaves 2 en este caso
l1 = len(x2[0]) #longitud de lista de valores
lista1 = []
dictio = {}
dictio2 = {}
for i in range(l1):
    
    for j in range(l2):
        dictio[x1[j]]=x2[j][i]
        dictio2.update(dictio)
        
    lista1.insert(i,dictio2)
    dictio2 ={}
    
    
        
        

    
print(lista1)



