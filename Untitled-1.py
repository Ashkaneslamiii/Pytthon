total = 0

while(True):   

    y = input()
    
    if y == "exit":
        if total==0:
            print(":( bye")
            break

        elif total!=0:

            print("you pressed exit", "\n","your total number is", total)
            break
        
    x = float(y)
    total = total + x
    print (total, "is total until now")