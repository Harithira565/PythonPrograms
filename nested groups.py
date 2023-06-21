eng=int(input("enter the mark:"))
math=int(input("enter the mark:"))
science=int(input("enter the mark:"))
soc=int(input("enter the mark:"))
if(eng>=30 and math>=30 and science>=30 and soc>=30):
    if(eng>80 and math>80 and science>80 and soc>80):
        print("science stream")
    elif(eng>80 and math>50 and science>50):
        print("commerce stream")
    elif(eng>80 and soc>80):
        print("humanities")
    else:
        print("invalid input")

