huevos = [46.5, 60.8, 58.7, 70.0, 49.8]
'''Los huevos de categoría A son clasificados según su peso como:
Huevos A cuyo peso va desde los 53 g. hasta un peso menor de 60 g.
Huevos AA cuyo peso va desde los 60 g. hasta un peso menor de 67 g.
Huevos AAA cuyo peso está por encima de los 67 g.
y los tipo B y C o BC como:
Huevos B cuyo peso va desde 46 g. hasta un peso menor de 53 g.
Huevos C cuyo peso es menor de 46 g.
'''
def calcular_bandejas(a):
    a = int(a)



def clasificacion_huevos(a):
    a = list(a)
    A = []
    for i in range(len(a)):
        if (53<=i<60):
            