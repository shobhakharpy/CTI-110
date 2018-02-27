# CTI 110
# Shobhakhar Adhikari
# 02/ 27/ 2018
# P3HW2: Software Sales

# define variables and get input

quantity = float(input("Enter the number of packages purchased:"))
unitPrice = 99
totalPrice = quantity * unitPrice

# calculations or decision structure
if quantity>=10 and quantity <20:
    discount = 0.1 * totalPrice
    totalCost = totalPrice - discount
    print("The total purchased cost with the discount applied is:$",format(totalCost,',.2f'))
elif quantity >= 20 and quantity < 50:
    discount = 0.2 * totalPrice
    totalCost = totalPrice - discount
    print("The total purchased cost with the discount applied is:$",format(totalCost,',.2f'))
elif quantity>= 50 and quantity <100:
    discount = 0.3 * totalPrice
    totalCost = totalPrice - discount
    print("The total purchased cost with the discount applied is:$",format(totalCost,',.2f'))
elif quantity>=100:
    discount = 0.4 * totalPrice
    totalCost = totalPrice - discount
    print("The total purchased cost with the discount applied is:$",format(totalCost,',.2f'))


    

# output or display result
