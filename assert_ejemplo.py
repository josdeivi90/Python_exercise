'''import math

try:
    x = float(input("ingrese el numero = "))
    assert x >= 0.0  # en esta linea de codigo me aseguro que mi numero sea si o si mayor que 0.0
    x = math.sqrt(x)
    print(x)
except AssertionError:
    print("la hemos cagado mi llave")'''

from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

# debemos estar seguros de ese angulo != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))