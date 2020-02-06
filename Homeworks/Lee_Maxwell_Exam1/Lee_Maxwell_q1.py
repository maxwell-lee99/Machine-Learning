#Maxwell Lee
#Exam
#Q1

x = float(input("Enter the amount in dollars and cents that is less than $100:"))
print("Change for $" + str(x))
print("Twenty Ten Five One Quarter Dime Nickel Penny")
checktw=int(x/20)+1
checkten=int(x/10)+1
checkf=int(x/5)+1
checkone=int(x/1)+1
checkq=int(x/.25)+1
checkd=int(x/.1)+1
checkn=int(x/.05)+1
checkp=int(x/.01)+1  #these are done to set the range for the for loop at the maximum possible value for the given change based on the input, runs much faster
checkx=x*100 #takes x value and multiplies by 100 as I was having issues with roundoff error


for tw in range(0,checktw):
    for ten in range(0,checkten):
        for f in range(0,checkf):
            for one in range(0,checkone):
                for q in range(0,checkq):
                    for d in range(0,checkd):
                        for n in range(0,checkn):
                            for p in range(0,checkp):
                                if (2000*tw+1000*ten+500*f+100*one+25*q+10*d+5*n+1*p) == checkx:
                                    print(tw,ten,f,one,q,d,n,p)



