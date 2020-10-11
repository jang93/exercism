from math import sqrt
import math as m


def largest(min_factor, max_factor):
    return palindrome(min_factor, max_factor, smallest=False)

def smallest(min_factor, max_factor):
    return palindrome(min_factor, max_factor)

def is_palindrome(num):
    num = str(num)
    left = 0
    right = len(num) - 1
    while left <= right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True

def get_factors(num, min_factor, max_factor):
    factors = []
    for i in range(min_factor, min(max_factor+1, int(m.sqrt(num))+1)):
        if num % i == 0 and num / i <= max_factor:
            factors.append([i, num//i])
    return factors

def palindrome(min_factor, max_factor, smallest=True):
    if max_factor < min_factor:
        raise ValueError('Max factor cannot be smaller than Min factor')
    args = (min_factor**2, max_factor**2+1, 1) if smallest else (max_factor**2, min_factor**2-1, -1)
    for product in range(*args):
        if is_palindrome(product):
            factors = get_factors(product, min_factor, max_factor)
            if len(factors) > 0:
                return product, factors
    return None, []