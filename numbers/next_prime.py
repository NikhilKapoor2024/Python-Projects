import math

"""
Next Prime Number
-------------------
Finds the next Prime Number until user stops
"""
def isPrime(num):
    """
    Finds out if the number is prime
    """
    # check if number is the lowest prime number
    if num <= 1:
        return False
    flag = True

    # check divisibility from 2 to sqrt(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = False
            break
    
    return flag


def main():
    """
    Main driver function
    """
    prime_nums = []
    for i in range(2, 100):
        if isPrime(i):
            prime_nums.append(i)
    
    for n in prime_nums:
        user_input = input("Type Y/N if you want to see the next prime number or not: ")
        if user_input.lower() == 'y':
            print(n)
        else:
            break

if __name__ == "__main__":
    main()

