x = int(input())

y = int(x/3600)

temp1 = y
temp2 = y

z = int(temp1/60)
d = int(temp2 % 60)

print(" time is ", y, ":", z, ":", d)

