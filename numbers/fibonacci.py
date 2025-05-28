import math
"""
Fibonacci Sequence:
---------------------
Generates the Fibonacci sequence to the Nth digit
"""

fib_seq = []
fib_seq.append(0)
fib_seq.append(1)
n = 2

end = int(input("Fibonacci Sequence up to the Nth digit: "))
while n < end:
    value = fib_seq[n - 2] + fib_seq[n - 1]
    fib_seq.append(value)
    n += 1

print(fib_seq)
