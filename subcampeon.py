n = int(input("cuantos valores me van a pasar = "))
#h = [1,2,3,4,5,6,6,89,7]
#h = sorted(h)
sub = []
arr = list(map(int, input("medidas = ").split()))
arr = sorted(arr)
maximo = -9999999999
for i in range(n):
    if(arr[i]>maximo):
        maximo = arr[i]
        sub.append(maximo)

print(sub[-2])