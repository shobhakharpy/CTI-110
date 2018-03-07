# CTI 110
# Shobhakhar Adhikari
# Practice Assignment

# define varaibles and get the input

def MoneyCounting ():
    p = int(input("Enter the number of pennies:"))
    n = int(input("Enter the number of nickels:"))
    d = int(input("Enter the number of dimes:"))
    q = int(input("Enter the number of quarters:"))
    
# Calculations and decision structure
    amount = 0.01*p + 0.05*n + 0.1*d + 0.25*q

    if amount > 1:
        print("The amount is:",format(amount,',.2f'))
        print("Sorry! the amount is more than one dollar.")
    elif amount < 1:
        print("The amount is:",format(amount,',.2f'))
        print("Sorry! the amount is less than one dollar.")
    else:
        print("Congratulations! you won the game.\n The amount is exactly one dollar.")

MoneyCounting ()      
