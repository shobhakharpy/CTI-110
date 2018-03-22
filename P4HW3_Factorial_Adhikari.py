# CTI 110
# Shobhakhar Adhikari
# P4HW3
# Factorial

# input and define variables

num = int(input("Enter a non-negative integer:"))
y = 1
# for loop

for x in range(num,0,-1):
    y *= x
print("The factorial of", num, "is :", y)
