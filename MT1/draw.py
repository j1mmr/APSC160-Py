#program that creates a square cut in half from top left to bottom right. Left is '@'s and right is '.'s. The line is 'X's.

#What needs work:
#needs to add type check on input???
#figure out a way to add a softer error that reprompts user for correct input.

numRows = int(input("Please enter the number of rows (>1):   "))
while numRows<2:
    print("The number rows must be greater than 1.")
    numRows = int(input("Try again: "))
    pass

counterRow = 1
counterCol = 0
row=""
while counterRow < (numRows+1): #row counter
    while counterCol < numRows: #column counter
        if counterRow > (counterCol + 1): #check if left of line
            row+="@"
            pass

        elif counterCol == (counterRow - 1): #check if line
            row+="X"
            pass

        else: #check if right of line
            row+="."
            pass
        counterCol+=1;
        pass
    print(row) #print row
    row = ""  #reset row
    counterRow +=1
    counterCol = 0 #reset col count
    pass
