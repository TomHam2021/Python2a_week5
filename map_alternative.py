# Another alternative
# • Sometimes a list comprehension or generator expression is better than using map
# • Especially when the function is not already defined
# • One benefit of using a list comprehension is that we don’t have to convert the result to a list to print it

numbers = range(10)
even_numbers = [x * 2 for x in numbers]  # detta är "list comprehension"
odd_numbers = [x * 2 + 1 for x in numbers]

print(even_numbers)
print(odd_numbers)

# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#         [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
