# Map with *args
# • Map can apply multiple-argument functions when given multiple iterables
# • It will process one element at a time from all iterables, until it reaches the end of any iterable

numbers1 = range(10)
numbers2 = range(100)
# stegar bara igenom det kortaste rangen! dvs 0..9
sum = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sum))  # sum är en class men ändras till en list

# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
