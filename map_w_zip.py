# Implementing map with *args
# • You should always use the built-in map
# • However, this example gives a hint on how it works
# • Note how it uses zip, another built-in function
# • zip([1, 2], [3, 4]) = [(1, 3), (2, 4)]
# tar första elementet får varle lista och sedan andra elementet från varje lista..

def my_map(f, iterable, *iterables):  # egentligen behövs inte "*" här, funkar lika bra utan!
    for args in zip(iterable, *iterables):  # "*" behövs inte här heller..
        yield f(args)  # men här måstge "*" vara med!


# den sista 7:an får inte vara med..
result = my_map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6, 7])
print(list(result))

# Output: [5, 7, 9]
