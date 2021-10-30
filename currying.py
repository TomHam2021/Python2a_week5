# Currying
# • In Python, a function is an object that can be passed as argument or returned from another function
# • Currying is a concept that builds on this capability
# • Here add is a curried function (a function that returns a function) <-- OBS!!!!

# add = lambda a: lambda b: a + b
def add(a): return lambda b: a + b


add3 = add(3)   # denna blir samma sak som ovan, obs anropar add

# först skickas 3 till add( lambda a:) och sedan skickas 7 till add(lambda b:)  !!!
x = add(3)(7)
y = add3(7)
print(x, y)
# Output: 10 10
