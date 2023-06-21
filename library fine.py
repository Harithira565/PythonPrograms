days=int(input("enter the no of days:"))
if(days>=1 and days<=31):
   if(days>=1 and days<=5):
       charge=days*5
       print(charge)
   elif(days>=6 and days<=10):
       charge1=days*5*3
       print(charge1)
   elif(days>=11 and days<=15):
       charge2=days*5*3*4
       print(charge2)
   elif(days>15):
       charge3=days*5*3*4*5
       print(charge3)
else:
    print("no charge apllicable")
