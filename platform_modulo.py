'''Esta funcion me permite tener información de mi sistema operativo'''

from platform import machine, platform,processor, system, version, python_implementation, python_version,node

print(platform())
print(platform(1))
print(platform(0, 1))
print(platform(aliased = False, terse = True))
print(machine()=="AMD64")
print(processor())
print(system())
print(version())
print(node())
print(python_implementation())
print(python_version())