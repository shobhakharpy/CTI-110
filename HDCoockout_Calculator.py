# CTI 110
# Shobhakhar Adhikari
# Practice Assignment

# define varaibles and get the input

def HDCookout ():
    

    Num_ppl = int(input("Enter the number of people attending the cookout:"))



    # Calculations and decision structure

    x = Num_ppl//10 # gives the number without decimal after divided by 10
    a = Num_ppl%10 # gives the remainder after divided by 10
    y = Num_ppl//8 # gives the number without decimal after divided by 8
    b = Num_ppl%8  # gives the remainder after divided by 8


    if a < 10 and a > 0:
        Num_hotdogsp = x + 1
        leftover_hotdogs = 10 - a
    else:
        Num_hotdogsp = x
        leftover_hotdogs = 0
    if b < 8 and b >0:
        Num_hotdogbunsp = y + 1
        leftover_buns = 8 - b
    else:
        Num_hotdogbunsp = y
        leftover_buns = 0
    
# display output

    print("The minimum number of packages of hot dogs required is:",Num_hotdogsp)
    print("The minimum number of packages of hot dog buns required is:",Num_hotdogbunsp)
    print("The number of hot dogs leftover is:",leftover_hotdogs)
    print("The number of hot dog buns leftover is:",leftover_buns)
HDCookout()
