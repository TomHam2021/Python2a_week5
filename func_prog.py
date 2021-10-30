'''
# Functional composition
# • Lego is a popular toy because it’s so versatile
# • Similar to how Lego pieces can be combined, in functional programming it’s common to combine functions

def f(number): return number * 2
def g(number): return number + 1


x = 2
# print(f(2))  # detta ger --> 4
# print(g(2))  # detta ger --> 3

# skicka 2 till g(+1) --> 3 och vidare till f(*2) --> 6
y = f(g(x))
# skcika 2 till f(*2) --> 4 och vidare till g(+1) --> 5
z = g(f(x))
print(y, z)
# Output: 6 5
'''

# Lambda
# • Python supports anonymous functions with lambda
# • Useful to define simple functions
# lambda = anonymous function , parametern till lambda finns mellan "Lambda" och ":"
# nedan skickas number till functionerna, och number uppdateras och returneras

# obs att pylance ändrar från lambda... :D
# f = lambda number: number * 2
# g = lambda number: number + 1


def f(number): return number * 2
def g(number): return number + 1


x = 2
y = f(g(x))
z = g(f(x))
print(y, z)

# Output: 6 5
