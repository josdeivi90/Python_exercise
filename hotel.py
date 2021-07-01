habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)] 
'''etiqueto con false para decir si la pieza esta ocupada o no el hotel 
habitaciones, piso, edificio'''
habitaciones[1][3][12]=True
vacante=0
if (habitaciones[1][3] is not False ):
    vacante =+ 1
    

print(habitaciones[1][3])
print(vacante)