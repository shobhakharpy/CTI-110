# CTI 110
# Shobhakhar Adhikari
# For loop and While loop
# 03/15/2018


print("KPH\t MPH")
print("-------------") # table title with KPH and MPH

for num in range(60,131,10):
    MPH = num*0.6214
    print(num, '\t',format(MPH,'.1f'))

input("Enter any key to exit:")
