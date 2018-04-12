# CTI 110
# P5T1: Kilometer Converter

def main ():
    Km = float(input("Enter a distance in Kilometers:"))
    def show_miles(x):
        miles = x * 0.6214
        print ("The distance after converted to miles is:",format(miles,'.2f'))
    show_miles(Km)
main()
 
