# Filter
# • The filter function is another built-in that’s commonly used in functional programming
# • filter(function, iterable) -> iterator
# • It returns an iterator of the elements in the iterable that function evaluates to a truthy value for

numbers = range(10)
# obs att x % 2 görs på varje element i listan!
even_numbers = filter(lambda x: x % 2 == 0, numbers)
odd_numbers = filter(lambda x: x % 2, numbers)
# ovan är filter = x % 2 = 1
# nedan funkar på samma sätt!
# odd_numbers = filter(lambda x: x % 2 == 1, numbers)
print(list(even_numbers))
print(list(odd_numbers))

# Output: [0, 2, 4, 6, 8]
#         [1, 3, 5, 7, 9]

# for n in range(5):
#    print(n % 2)
# The modulo operator, when used with two positive integers, will return the remainder of standard
# 0/2=0 -> rest 0
# 1/2=0 -> rest 1
# 2/2=1 -> rest 0
# 3/2=1 -> rest 1
# 4/2=2 -> rest 0
# 5/2=2 -> rest 1
