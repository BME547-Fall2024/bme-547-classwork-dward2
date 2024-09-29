import math

def sqrt(n):
    if type(n) is not int:
        raise TypeError("The input to sqrt needs to be an integer type.")
        
    if n < -0:
        raise ValueError("The value of {} is negative.  "  
                         "It must be positive".format(n))
    return math.sqrt(n)
    