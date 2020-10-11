import math as m

def classify(number):
    if number <= 0:
        raise ValueError("number provided is not a natural number")
    elif number == 1:
        return 'deficient'
    aliquot_sum = sum((i for i in range(1, number//2+1) if number % i == 0))
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'deficient'
