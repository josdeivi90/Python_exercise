f_0 = 0
f_1 = 1
f_n = 0
print (f_0)
print (f_1)

while(f_n<50):
    f_n = f_0 + f_1
    if(f_n >=50):
        break
    print(f_n)
    f_0,f_1 = f_1,f_n

'''def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10):
    print(n, "->", fib(n))
'''