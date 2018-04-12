# CTI 110
# This program will convert a measure in feet to inches.
# P5T2: Feet to Inches converter
# Shobhakhar Adhikari
# 04/12/2018

def main ():
    Ft = float(input("Enter a measure in feet:"))
    def show_inches(x):
        inches = x * 12
        print ("The measure after converted to inches is:",format(inches,'.2f'))
    show_inches(Ft)
main()
 
