x = int(input("insert the number of students"))
avg = 0
scores = []
max = 0
min = 0
for i in range (x):
    y = int(input("insert the avegareg of student number"))

    scores.append (y)
    avg = avg + scores[i]

    if y > max:
        max = y
    elif y < min or min == 0:
        min = y


print("For",x,"students, average is equal to ", avg/x , "\n Maximum number is", max, "\n Minimum number is ", min)