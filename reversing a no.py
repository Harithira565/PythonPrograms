n=int(input("enter the no:"))
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
print("reversed no is:",r)
