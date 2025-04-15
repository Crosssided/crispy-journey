c = int(input("Number: "))

while c != 1.0:

    if c < 0:
        break

    if c % 2 == 0:
        c = c/2
    elif c % 2 == 1:
        c = 3 * c + 1
    
    print(c)

    

