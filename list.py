a=[1,14,"hi",67.8,45]
print(a)
print(len(a))
a.append(23)
a[3]=33
print(a)


b=[]
b.append(677)
print(b)

##using for range accesssing values in a list
a=[56,67,1,4,6,7]
for i in range(0,len(a)):
    print(a[i])

##without for range accessing values in a list
b=[34,12,1,90]
for i in b:
    print(i)

n=int(input("enter the number:"))
a=[]
for i in range(1,n+1):
   print(i)
   a.append(i)
print(a)


n=int(input("enter the no:"))
a=[]
for i in range(1,n+1):
    print(i**2)
    a.append(i**2)
print(a)



