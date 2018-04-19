# CTI 110
# Shobhakhar Adhikari
# P5HW2: Random Number Guessing Game

# this program generate a random number in range from 1 to 100 and let user to geuss it correct!

import random

def main ():
    Min = 1
    Max = 100
    ans = 'y'
    
    while ans == 'y':
        r = random.randint(Min,Max)  # generates random integer and assign it to var y.
        x = int(input("Please guess what the secret number is ranging from 1 to 100:"))
        if x == r:
            print("Congratulations! You guessed it right!")
        else:
            while x != r:
                
        
                if x > r:
                    print("Too high, try again.")
            
                else:
                    print("Too low, try again.")
                    
                
            
                x = int(input("Enter the number you want to guess again:"))

            print ("Congratulations! you guesses it right!")

        ans = input("Do you want to play this game over again?...please type y for yes or n for no:")
              
main()
