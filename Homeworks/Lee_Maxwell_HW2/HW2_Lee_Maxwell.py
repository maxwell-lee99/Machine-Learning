# Maxwell Lee
# ITP 449 Fall 2019
# HW2
# Question 1
print("Change for $1")

for quarter in range(5):
    for dime in range(11):
        for nickel in range(21):
            for penny in range(0,101,5):
                if (quarter*25 + dime*10 + nickel*5 + penny) == 100:
                    print(quarter, "quarters,",dime, "dimes,",nickel, "nickels,", penny, "pennies")


