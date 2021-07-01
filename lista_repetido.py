'''miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
Lista2 = []
l = len(miLista)
for i in range(l):
    if (miLista.count(i)>1):
        Lista2.append(i)
    else:
        continue
            


print("La lista solo con elementos únicos:")
print(miLista)
print(Lista2)'''

'''Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
'''

entrada = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
arr = dict(entrada)
for i in range(len(entrada)):
    if arr.keys() in entrada[i][0]:
       arr.update({entrada[i][0]:entrada[i][1]})
    else:
        continue


print(arr)


