import math

def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    
    if(n%2==0 or n%3==0):
        return False
    
    else:
        
        for i in range(5,int(math.sqrt(n))):
            if(n%i ==0 or n%(i+2)==0):
                return False
            i=i+6
        return True

def primeFactors(n): 
    facArr = set()

    # Print the number of two's that divide n 
    if (n%2 == 0):
        facArr.add(2)
        n = n // 2

    while n % 2 == 0: 
        n = n // 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            facArr.add(i)
            n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        facArr.add(n)

    return list(facArr)