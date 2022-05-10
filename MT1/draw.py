numRows = int(input("Please enter the number of rows:   "))
while numRows<2:
    print(int("try again"))
    numRows = input("enter")
    pass

counterRow = 1
counterCol = 0

while counterRow < numRows:
    while counterCol < numRows:
        if counterRow > (counterCol + 1):
            print("@")
            pass

        elif counterCol == (numRows + 1):
            print("X")
            pass

        else:
            print(".")
            pass
        counterCol+=1;
        pass
    print("\n")
    counterRow +=1
    pass
