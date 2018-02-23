# CTI 110
# Python 3 Exercise
# Shobhakhar Adhikari
# 02/22/2018

#define variables and get input

salary = int(input("Enter salary: "))

yearsonJob = int(input("Enter years worked: "))

# Calculation or decision structure

if salary >= 30000:
    if yearsonJob >= 2:
        print("You qualify for a loan.")
    else:
        print("You do not qualify for loan. you have to work two years or more.")
else:
    print("You do not qualify for loan. you do not earn enough.")
