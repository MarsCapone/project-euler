import euler
from fractions import gcd
import operator
import functools

# ----- Problem 1 ----- #
def pe1():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


# ----- Problem 2 ----- #
def pe2():
    return sum([i for i in euler.fibonacci(4000000) if i % 2 == 0])


# ----- Problem 4 ----- #
def pe4(): 
    max_palindrome = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            val = a * b
            if euler.isPalindrome(val) and val > max_palindrome:
                max_palindrome = val
    return max_palindrome


# ----- Problem 5 ----- #
def pe5():
    # worked out minimum requirement of prime factors by hand. 
    min_factors = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
    return functools.reduce(operator.mul, min_factors, 1)


# ----- Problem 6 ----- #
def pe6():
    return abs(sum([i * i for i in range(1, 101)]) - (sum(range(1, 101))) ** 2)



# ----- Problem 33 ----- #
def pe33():
    denproduct = 1
    nomproduct = 1
    for i in range(10):
        for den in range(i):
            for nom in range(den):
                if (nom * 10 + i) * den == nom * (i * 10 + den):
                    denproduct *= den
                    nomproduct *= nom
    return denproduct / gcd(nomproduct, denproduct)
