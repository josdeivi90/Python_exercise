'''countries = set()
for n in range(int(input("here = "))):
    countries.add(input("ahora si la lista"))

print(len(countries))'''
'''
#.remove(x)

s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.remove(5)
print (s)

print (s.remove(4))

print (s," aqui ")
#set([1, 2, 3, 6, 7, 8, 9])
#s.remove(0) ----> va a botar un error

#.discard(x)
hace lo mismo que remove a diferencia que cuando le pido que borre algo que no existe, no bota error
#.pop()
s.pop(3)
print(s)'''
'''
n = int(input())
s = set()
for i in range(n):
    s.add(int(input("ahora si la lista")))

print(s)
#s = set(map(int, input().split()))
'''
n = int(input())
s = set(map(int, input().split())) 
print (s)
for i in range(int(input('lista de instrucciones'))):
    eval('s.{0}({1})'.format(*input('instruccion').split()+['']))

print(sum(s))
