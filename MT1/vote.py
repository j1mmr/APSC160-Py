#Simple program for tallying votes

#What needs to be fixed
#same as the other code from mt1, need to find a way to soft fail when inputing a non-int (if possible)


def input_func():
    user_input = int(input())
    while user_input != 1 and user_input != 2 and user_input != 0:
        print("Illegal input. Try again.")
        user_input = int(input())
        pass
    return user_input
    pass


count_no = 0
count_yes = 0
print ("Please enter your vote (1 for Yes, 2 for No, 0 to end voting):")
user_choice = input_func()
while user_choice != 0:

    if user_choice == 1:
        count_yes += 1
        pass

    else:
        count_no += 1
        pass

    user_choice = input_func()
    pass


str = "For: " + str(count_yes) + " Against: " + str(count_no) #starts output string with results of vote

if count_no < count_yes:
    str += " Policy has passed."
    pass
elif count_no > count_yes:
    str += " Policy has failed."
    pass
else:
    str += " Policy will be revisited at a later date."
    pass

print(str) #prints output string
