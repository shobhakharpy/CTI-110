#CTI 110
# Shobhakhar Adhikari
# 03/02/2018
# Book Club Points

# define variable and get the input

x = int(input("Enter the number of books that you have purchased this month: "))

# calculations or decision structure

if x == 0 or x == 1:
    print("You have earned 0 points.")
elif x == 2 or x == 3:
    print("You have earned 5 points.")
elif x == 4 or x ==5:
    print("You have earned 15 points.")
elif x == 6 or x == 7:
    print("You have earned 30 points.")
else:
    print("You have earned 60 points.")
