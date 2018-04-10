import random
MIN = 1
MAX = 6
ans = "yes"
while ans == "Yes" or ans ==  "yes":
    
    print (random.randint(MIN, MAX))
    print (random.randint(MIN, MAX))
    ans = input("Do you want to roll a die again twice?")
