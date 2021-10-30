# Reduce
# • When programming it’s common to accumulate a value by stepping through a collection
# • Summing a list of numbers or concatenating strings are examples of this
# • Reduce is a generalization of this concept

from functools import reduce


def factorial(n):
    # denna är knepig...
    return reduce(lambda x, y: x * y, range(1, n+1), 1)


print(factorial(10))

# Output: 3628800
