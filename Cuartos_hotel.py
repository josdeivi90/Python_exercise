#k, rooms, single, multiple = input(), input().split(), set(), set() 
# este codigo va a servir pero va a demorar mucho mas

k = input()
cuartos = input().split()
capitan = set()
multiple = set()
for room in cuartos: 
    if room not in capitan:
        capitan.add(room)  
    else:
         multiple.add(room)

print(capitan.difference(multiple).pop())