n=int(input("enter the no:"))
a=1
for i in range(1,n+1):
    a=a*i
print("the factorial of given no is:",a)


##sum of n nos

n=int(input("enter the no:"))
a=0
for i in range(1,n+1):
    a=a+i
print(a)

##sum of even nos
n=int(input("enter the no:"))
a=2
i=2
for i in range(n):
    a=a+i
    i=i+2
print(a)
