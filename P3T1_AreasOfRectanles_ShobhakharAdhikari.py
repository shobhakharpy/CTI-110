# CTI 110
# Shobhakhar Adhikari
# P3T1 Areas of Rectangles
# 02/27/ 2018

# define variables and get input

length1 = float(input('Enter the length of first rectangle in feet: '))

width1 = float(input('Enter the width of first rectangle in feet: '))

length2 = float(input('Enter the length of second rectangle in feet: '))

width2 = float(input('Enter the length of second rectangle in feet: '))

# calculations or decision structure

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print('The first rectangle has larger area.')
elif area1 == area2:
    print('Both rectangles have equal area.')
else:
    print('The second rectanle has the larger area.')


# Output or display result
