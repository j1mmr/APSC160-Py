LastValue = 2 #again this was not given, supposed to be a constant given by the test environment

def nextValue(n): #this was not given, so I created the simplest one possible (just to test)
    return n-1
    pass

print("Please enter the starting value to be computed")
value = int(input())

while value != LastValue:
    value = nextValue(value)
    print(value)
    pass
