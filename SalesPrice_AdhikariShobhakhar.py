# CTI 110
# Python 2 Exercise
# Shobhakhar Adhikari
# 02/20/2018

# input original price of an item

originalPrice = float(input('Enter the original price in dollars :$'))

# Calculate discount

discount = 0.2 * originalPrice

# Calcualte sales price

salesPrice = originalPrice - discount

# Display result
print ('The sales price is : $',format(salesPrice,',.2f'))
