year=int(input("enter the year:"))
if(year%100==0):
         if(year%400==0):
              print("leap year and century year")
         else:
             print("Not a leap year")
else:
    if(year%4==0):
        print("leap year")
    else:
        print("not a leap year")
