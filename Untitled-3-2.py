n = int(input())
a = 0
b = 1
numbers = []

if n == 0:
    numbers.append(a)
    print(numbers)
if n == 1:
    numbers.append(a)
    numbers.append(b)
    print(numbers)
else:
    numbers.append(a)
    numbers.append(b)
    for i in range(n-2): 
        c = a + b
        numbers.append(c)
        print(numbers)
        a = b
        b = c 


