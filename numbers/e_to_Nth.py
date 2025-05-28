import math
"""
e To The Nth:
--------------
prints e to the Nth digit
"""
while True:
    n = int(input("PI to the Nth digit: "))
    if (n > 10):
        print("limit reached")
    else:
        break
e = math.e

ans = e ** n
print(f"{n:.{n}f}")