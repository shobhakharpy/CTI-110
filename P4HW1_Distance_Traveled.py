#CTI 110
#Shobhakhar Adhikari
# P4HW1: DIstance Traveled

#ask user to enter speed of a vehicle and number of hours it has traveled.

speed = float(input("Enter the speed of the vehicle in mph:"))

hours = int(input("Enter the number of hours traveled:"))

print("Hour \t Distance Traveled")
print("--------------------------")

for hours in range(1,hours+1):
    distance = speed * hours
    print(hours,'\t', distance)
    
