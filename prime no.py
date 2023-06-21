n=int(input("enter the no:"))
for i in range(2,n+1):
   if(n%i==0):
        print(n)
        print("not a prime no")
   else:
       print(n,"prime no")
