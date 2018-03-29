# CTI 110
# Shobhakhar Adhikari
# Fibonachi Sequence

def fib(n):
    
    a = 0
    b = 1

    for x in range (n):
        print (a, end=' ')
        a,b = b, a+b
        
fib(10)
    
    
