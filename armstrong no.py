n=int(input("enter the no:"))
b=n
s=0
while(n!=0):
    d=n%10
    n=n//10
    s=s+d**3
print(s)
print(n)
if(s==b):
    print("armstrong no")

