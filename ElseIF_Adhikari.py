# CTI 110
# Python 3 Exercise
# Shobhakhar Adhikari
# 02/222/2018

# Get the test scores

firstScore = float(input('Enter your first test score:'))
secondScore = float(input('Enter your second test score:'))
thirdScore = float(input('Enter your third test score:'))

# Calculate average

average = (firstScore + secondScore + thirdScore)/3


# Display the average
print ('The average test score is :',format(average,'.1f'))

if average >= 90:
    print('Congratulations! You have passed with the grade of A.')
elif average >= 80:
    print('Congratulations! you have passed with the grade of B.')
elif average >= 70:
    print('Congratulations! you have passed with the grade of C.')
elif average >= 60:
    print('Congratulations! you have passed with the grade of D.')
else:
    print('Sorry, you failed the test.')
    

