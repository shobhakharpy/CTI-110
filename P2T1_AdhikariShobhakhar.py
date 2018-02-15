# CTI-110
# P2T1 - Sales Prediction
# Shobhakhar Adhikari
# 02/13/2018


# Get the projected amount of sales.
TotalSales = float(input('Enter the projected amount of total sales in dollars:'))

# calcualte the profit.
AnnualProfit = 0.23 * TotalSales

# Display the profit.
print ('The profit is : $',format(AnnualProfit,',.2f'))
