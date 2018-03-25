# CTI 110
# Shobhakhar Adhikari
# P4T2
# Bug Collector
# 03/ 25/2018

# Intitialize the accumulator
total = 0

# get the bugs collected for each day

for day in range(1,8):
    print("Enter the number of bugs collected on day",day)
    bugs = int(input())
    total += bugs

# display the result

print ("The total number of bugs collected is:",total)
