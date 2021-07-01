#A = [[1, 4, 5], 
#    [-5, 8, 9],
#    [ 5, 7, 2]]

#for i in range(len(A)):
#    for j in range(len(A[:])):
#        print(A[i][j])

#a partir de la matriz, generar dos listas una para los números pares otra para los impares e imprimir cada una de las listas por aparte 
'''
A=[[87,-5,654],
	    [0 , 5,  1],
	    [-56,21,92]]
even = []
odd = []

for i in range(len(A)):
        for j in range(len(A[:])):
            if(A[i][j]%2 == 0):
                even.append(A[i][j])
            else:
                odd.append(A[i][j])

print("los pares son: ",even,"\n")
print("los impares son: ",odd,"\n")'''
A = []
                
'''for i in range(5):
    print("* "*i)
for j in range(5,0, -1):
    print("* "*j)'''

miLista = [10,50,11,89,74,50,66,74,28,94,16] 
#miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
Lista2 = []
l = len(miLista)
for i in miLista:
    if (miLista.count(i)>1 and i not in Lista2 ):
        Lista2.append(i)
    else:
        continue


print(max(miLista))
print(min(miLista))
print(Lista2)