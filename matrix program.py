a=[]
c=[]
n=int(input("enter the row and col:"))
for i in range(n):
    a.append([])
    for j in range(n):
        b=int(input("enter the no:"))
        a[i].append(b)
print(a)
n=int(input("enter the row and col:"))
for i in range(n):
    c.append([])
    for j in range(n):
        e=int(input("enter the no:"))
        c[i].append(e)
print(c)

d=[]
for i in range(n):
    d.append([])
    for j in range(n):
       e=c[i][j]+a[i][j]
       d[i].append(e)
print(d)



