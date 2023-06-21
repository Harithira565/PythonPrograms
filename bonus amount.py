salary=int(input("enter the salary:"))
years=int(input("enter the years of service:"))
if(years>10):
        bonus=10/100*salary
        print("bonus=",bonus)
        netBonus=bonus+salary
        print("net bonus amount=",netBonus)
elif(years>=6 and years<=10):
        bonus=8/100*salary
        print("bonus=",bonus)
        netBonus=bonus+salary
        print("net bonus amount=",netBonus)
else:
        bonus=5/100*salary
        print("bonus=",bonus)
        netBonus=bonus+salary
        print("net bonus amount=",netBonus)
