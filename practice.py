A=int(input("enter the no:"))
B=int(input("enter the no:"))
C=int(input("enter the no:"))
d1=A%10
d2=B%10
d3=C%10
if(d1>d2 and d1>d3):
    print(A)
elif(d2>d1 and d2>d3):
    print(B)
elif(d3>d1 and d3>d2):
    print(C)


A=int(input("enter the no:"))
B=int(input("enter the no:"))
C=int(input("enter the no:"))
if(A>B and  A>C):
    if(B>C):
        print(B)
    else:
        print(C)
elif(B>A and B>C):
    if(A>C):
        print(A)
    else:
        print(C)
elif(C>A and C>B):
    if(A>B):
        print(A)
    else:
        print(B)
 





   
    
