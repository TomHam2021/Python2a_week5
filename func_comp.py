# Lambda with zero or multiple arguments
# • Lambda functions can have any number of arguments

# f = lambda a, b, c: a + b + c   # input = a,b,c och returneras = a+b+c
# g = lambda *args: sum(args)     # samma som ovan!
# h = lambda: sum((1, 2, 3))      # här skickas inget till funtionen, utan istället returneras 6
def f(a, b, c): return a + b + c


g = lambda *args: sum(args)
def h(): return sum((1, 2, 3))


print(f(1, 2, 3))
print(g(1, 2, 3))
print(h())
print(f('1', '2', '3'))  # obs deta är strings(!) som slås ihop
# Output: 6
#         6
#         6
#         123
