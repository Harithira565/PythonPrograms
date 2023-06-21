i=0
while(i<7):
    if(i==4):
        break
    print(i)
    i=i+1
print("completed")



##continue
for i in range(0,7):
    if(i==4):
        continue
    print(i)
else:
    print("else block")

##break
for i in range(0,7):
    if(i==4):
        break
    print(i)
else:
    print("else block")

##continue

i=0
while(i<7):
    if(i==4):
        i=i+1
        continue
    i=i+1
    print(i)
print("completed")




