eng=int(input("enter the mark:"))
math=int(input("enter the mark:"))
science=int(input("enter the mark:"))
soc=int(input("enter the mark:"))
if(eng>=35 and math>=35 and science>=35 and soc>=35):
    if(eng>80 and math>80 and science>80 and soc>80):
        print("science stream")
    elif(eng>80 and math>50 and soc>=35 and science>50):
        print("commerce stream")
    elif(eng>80 and soc>80 and science>=35 and math>=35):
        print("humanities")
else:
    print("invalid input")
