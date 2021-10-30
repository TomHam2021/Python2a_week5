def my_map(f, iterable):
    for x in iterable:
        yield f(x)


result = my_map(lambda x: x + 10, [1, 2, 3])
print(list(result))

# Output: [11, 12, 13]
