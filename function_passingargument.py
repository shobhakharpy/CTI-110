fName = input("Please enter first name:")

lName = input("Please enter last name:")

def display (x,y):
    print("Welcome", x,y)
display(fName,lName)

pay_rate = float(input("\n Please enter pay rate:"))

hours = float(input("\n Please enter hours worked:"))
print()
def gross_pay (x, y):
    grossPay = x * y
    print("\n Your gross pay is : ", grossPay)

gross_pay (pay_rate, hours)
