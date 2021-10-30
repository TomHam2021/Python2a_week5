# Revisiting map
# • Map, zip, filter, reduce, etc. can all be implemented using recursion

# denna är knepig...
'''
def my_map(f, iterable):
    try:
        arg, *rest = iterable
    except ValueError:
        return []
    result = my_map(f, rest)
    return [f(arg), *result]


print(my_map(lambda x: x + 10, [1, 2, 3]))
# Output: [11, 12, 13]
'''

# Revisiting map… again!
# • Recursion can also happen in an inner function
# • This time we allow multiple iterables (again)


def my_map(f, iterable, *iterables):
    def inner(zipped):
        try:
            args, *rest = zipped
        except ValueError:
            return []
        return [f(*args), *inner(rest)]
    return inner(zip(iterable, *iterables))


print(my_map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6, 7]))
# Output: [5, 7, 9]
