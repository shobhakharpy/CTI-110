# CTI 110
# Shobhakhar Adhikari
# 02/ 27/ 2018

# define variable and get input

score = float(input("Enter your test score:"))

# calculations or decision structure

if score >= 90:
    print("Your grade is A.")
else:
    if score >= 80:
        print ("Your grade is B.")
    else:
        if score >= 70:
            print("Your grade is C.")
        else:
            if score >= 60:
                print("Your grade is D.")
            else:
                print("Your grade is F.")
