#CTI 110
# Shobhakhar Adhikari
# 03/02/2018
# Body Mass Index

# define variable and get the input

weight = float(input(" Enter your weight in pounds: "))
height = float(input(" Enter your height in inches: "))

# calculations or decision structure
BMI = weight * 703/height**2

print ("The BMI is:",format(BMI,',.2f'))
if BMI >= 18.5 and BMI <= 25:
    print("You have optimal weight.")
elif BMI < 18.5:
    print("You are underweight.")
else:
    print("You are overweight .")

