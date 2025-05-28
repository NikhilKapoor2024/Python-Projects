import math
"""
Prime Factorization:
---------------------
Finds all Prime Factors of a number and display them
"""

prime_factors = []
n = int(input("Enter a number to find its Prime Factors: "))

def primeFactors(n):
    # if+while n is even
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    
    #if+while n is odd
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    
    #if n is a prime number greater than 2
    if n > 2:
        prime_factors.append(n)

primeFactors(n)
print(prime_factors)
