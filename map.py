# Map
# • Loops are useful but often depend on side effects
# • One common alternative is to apply a function to every element of an iterable (list, dict or whatever)
# • Map is a built-in function that does exactly this
# • It returns a map object, that can be converted to a list

# 0 .. 9  , detta blir en class  meni print satsen nedan så ändras den till list-typ!
numbers = range(10)
# x*2 kommer att göras på varje element i listan numbers! man slipper använda for-loop!
even_numbers = map(lambda x: x * 2, numbers)
odd_numbers = map(lambda x: x * 2 + 1, numbers)
print(list(even_numbers))
print(list(odd_numbers))
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#         [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
