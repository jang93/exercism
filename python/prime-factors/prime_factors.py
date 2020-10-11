import math as m

def factors(value):
    if value == 1:
        return []
    for i in range(2, value+1):
        if value % i == 0:
            prime_factors = [i]
            prime_factors.extend(factors(value//i))
            return prime_factors
    return []
