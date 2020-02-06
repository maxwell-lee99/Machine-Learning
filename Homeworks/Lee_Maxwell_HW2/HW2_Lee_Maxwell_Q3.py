# Maxwell Lee
# ITP 449 Fall 2019
# HW2
# Question 3
access = False
symbols = ['-','!','@','#','$']
while access == False:
    x = input("Please enter a password with the following requirements" '\n'
              "Must be at least 8 characters long" '\n'
              "Must contain both uppercase and lowercase letters" '\n'
              "Must contain at least one number between 0-9" '\n'
              "Must contain a special character -,!,@,#,$: ")
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    check5 = 0
    length = len(x)
    for c in range(0,length):
        if length >= 8:
            check1 = 1
        if x[c].isupper():
            check2 = 1
        if x[c].islower():
            check3 = 1
        if x[c].isdigit():
            check4 = 1
        if x[c] in symbols:
            check5 = 1
    if check1+check2+check3+check4+check5==5:
        access= True
    if check1 == 0:
        print("Must be at least 8 characters long")
    if check2 == 0:
        print("Must contain an uppercase letter")
    if check3 == 0:
        print("Must contain a lowercase letter")
    if check4 == 0:
        print("Must contain a number")
    if check5 == 0:
        print("Must contain a special character -,!,@,#,$")

print("Access Granted")