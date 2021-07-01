
    #studiantes = []
    #for g in range(int(input("cuantos quieres = "))):
    #    name = input("nombre = ")
    #    score = float(input("score = "))
    #    studiantes.append([name,score])
studiantes = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    
print(studiantes)    #lista = [[0,1]= 0 , [0,1] = 1, [0,1] =2,[0,1] = 3 ]
estudiantes2 = dict(studiantes)

notas = estudiantes2.values()
notas = list(notas)
notas = sorted(notas) #arreglo de menor a mayor  [37.2, 37.21, 37.21, 39, 41]
notas2 = []
nota_final = []

    #elimino el valor mas pequeño
for i in notas:
    if(i != min(notas)):
        notas2.append(i)
    else:
        continue

    #hago el vector con mis penultimos valores  [37.21, 37.21, 39, 41]
for j in notas2:
    if(j == min(notas2)):
        nota_final.append(j)
    else:
        continue

finales = []
    # creo el dict con solo las claves que necesito [37.21, 37.21]
for k in range(len(studiantes)):
    if( studiantes[k][1] in nota_final):
        finales.append(studiantes[k][0])

finales = sorted(finales)
for i in finales:
    print (i)

  




