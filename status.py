

number = int(input("Please enter a number:"))

def ifeven (num):
    if  (num % 2) == 0:

        print ("Number is even")

        status = True
    else:
        print ("Number is odd")

        status = False

    return status

stat = ifeven(number)

print("status is:",stat)
