# CTI 110
# Shobhakhar Adhikari
# Python 5
# Automobile Costs

# define variables and get input

loan_payment = float(input("Enter the monthly cost of your loan payment in dollars:$"))
insurance = float(input("Enter the monthly cost of your Insurance in dollars:$"))
gas = float(input("Enter the monthly cost in gas in dollars:$"))
oil = float(input("Enter the monthly cost of Oil in dollars:$"))
tires = float(input("Enter the monthly cost for tires in dollars:$"))
maintenance = float(input("Enter the monthly cost of maintenance in dollars:$"))

def total_cost ( a,b,c,d,e,f):
    totalCost = a+b+c+d+e+f
    print("\n Your total cost of these expenses is:$", totalCost)

total_cost (loan_payment, insurance, gas, oil, tires, maintenance)
