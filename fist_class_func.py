# First-class functions
# • In the previous week we looked at how to define decorators using outer and inner functions
# • The outer function accepted a function as argument and returned the inner function as a value
# • Allowing functions to be used as arguments and return values is called having first-class functions

def call_twice(f):
    return lambda x: f(f(x))


multiply_by_four = call_twice(lambda x: x * 2)

print(multiply_by_four(10))
#Output: 40
