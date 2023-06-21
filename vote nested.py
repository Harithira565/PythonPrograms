age=int(input("enter the age:"))
if(age>0 and age<=100):
    if(age>=18):
        print("eligible to vote")
    else:
        print("not eligible to vote")
else:
    print("invalid input")
