x = int(input())

temp1 = int(x%3600)
y = int(x/3600)
z = int(temp1/60)
d = int(temp1 % 60)

print(" time is ", y, ":", z, ":", d)

