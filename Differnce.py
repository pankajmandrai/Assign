#find the difference between the sum of the squares of the first N natural numbers and the square of the sum.

def diff(n): 
    i = (n *(n+1)*(2*n+1))/6 
    m = (n*(n+1))/2 
    m = m**2
    p = abs(i-m) 
    return p  
print(diff(3)) #20
