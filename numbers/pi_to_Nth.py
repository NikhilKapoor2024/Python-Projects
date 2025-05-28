"""
PI To The Nth Digit
----------------------
A program that calculates PI to the Nth digit up to a decimal
"""
import math

while True:
    n = int(input("PI to the Nth digit: "))
    if (n > 10):
        print("limit reached")
    else:
        break

pi = math.pi
ans = pi ** n
print(f"{ans:.{n}f}")
