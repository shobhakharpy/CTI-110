import circle
import rectangle
def main():
    choice = menu()
    if choice == 1:
        radius = float(input("Enter the radius of the circle:"))
        My_area = circle.area(radius)
        print("The area of a circle is:",format(My_area,'.2f'))
        
    elif choice ==2:
        radius = float(input("Enter the radius of the circle:"))
        My_circum = circle.circum(radius)
        print("The circumference of a circle is:",format(My_circum,'.2f'))
    elif choice ==3:
        length = float(input("Enter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        My_area = rectangle.area(length,width)
        print("The area of the rectangle is:",format(My_area,'.2f'))
    elif choice ==4:
        length = float(input("Enter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        My_peri = rectangle.perimeter(length,width)
        print("The Perimeter of the rectangle is:",format(My_peri,'.2f'))
    else:
        print("Quit")
        
        
        
        

def menu():
    print("1 Area of a Circle")
    print ("2 Circumference of a circle")
    print ("3 Area of a rectangle")
    print ("4 Perimeter of a recangle")
    print ("5 Quit")

    choice = int(input("Enter the choice number from the list of above menu choices:"))
    return choice
main()
input ()
