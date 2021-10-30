# Recursion
# • A function in python can call itself
# • In pure functional programming this can be used to avoid using procedural loops
# • Often elegant but can be hard to read
# • Beware infinite recursion and high memory usage
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(10))
# Output: 3628800
