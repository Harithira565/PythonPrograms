traffic_light=input("enter the light:")


if(traffic_light=="green" or  traffic_light=="GREEN" ):
    print("Car is allowed to go")
elif(traffic_light=="yellow" or traffic_light=="YELLOW"):
    print("Car has to wait")
elif(traffic_light=="red" or "RED"):
    print("Car has to stop")
else:
    print("Unrecognized signal")
