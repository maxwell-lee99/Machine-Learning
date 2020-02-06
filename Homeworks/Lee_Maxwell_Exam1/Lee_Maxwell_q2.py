import os
import pandas
import matplotlib.pyplot as plt

fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2) #setting empty figure with two plots

principle = float(input("Loan amount: "))
interestrate = float(input("Interest rate: "))
years = float(input("Years: "))
extra = float(input("Enter the amount of your extra payment each month:"))#having the user inputting the necessary information as floating point numbers

monthlyir = (interestrate/100)/12
monthlypayment = (monthlyir + (monthlyir/((1+monthlyir)**(years*12)-1)))*principle
finalpay = round(monthlypayment,2) #running formula to calculate monthly payment and rounding it so that it is
                                    #displayed as a 2 digit decimal for currency

print("Your monthly payment is: $" + str(finalpay)) #printing out rounded monthly payment

print("Here is your loan history.")
print("Month    Interest        Balance         Extra")

months=int(years*12) #calculating the number of months the loan is for

x=[]
y=[]
z=[] #casting x,y,z as empty lists, x will be interest paid, y will be loan balance, z will be months

for i in range(1, months+1):
    interest=principle*monthlyir
    principle = principle - monthlypayment + interest - extra #formula for remaining principle
    x.append(interest)
    y.append(principle)
    z.append(i)
    if principle < .01: #forces program to break and sets principle to 0 if balance is less than a penny
        extra = round(extra+principle,2)
        principle = 0
        print(i, "      ", round(interest, 2), "        ",round(principle, 2), "        ",extra)
        break
    else:
        print(i, "      ", round(interest, 2), "        ",round(principle, 2), "        ",extra)




    #running a for loop for the number of months the loan is for
                                                #and appending the empty list to add corresponding information

ax1.plot(z,x,
         color='b',
         marker='o',
         markersize=2)
ax1.set_xlabel('Month')
ax1.set_ylabel('Interest paid') #plotting month and interest with the appropriate color, marker, and size to match picture

ax2.plot(z,y,
         color='r',
         marker='o',
         markersize=2)
ax2.set_xlabel('Month')
ax2.set_ylabel('Loan Balance') #plotting month and balance with the appropriate color, marker, and size to match picture

fig.suptitle('Lee_Maxwell_q2')
plt.show()
