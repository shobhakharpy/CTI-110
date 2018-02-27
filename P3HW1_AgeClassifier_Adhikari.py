# CTI 110
# Shobhakhar Adhikari
# P3HW1 Age Classifier
# 02/27/ 2018

# define variables and get input

age = float(input('Enter the age of a person in years: '))


# calculations or decision structure


if age <= 1:
    print('The person is an infant.')
else:
    if age <13:
        print('The person is a child.')
    else:
        if age <20:
            print('The person is a teenager.')
        else:
            print('The person is an adult.')


# Output or display result
