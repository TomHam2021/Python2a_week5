'''
# funtional programming undviker for-loopar men måste inte inehålla rekursiva anrop

def fib(n, a=0, b=1):
    return a if n < 1 else \
        b if n < 2 else \
        fib(n - 1, b, a + b)


print(fib(100))
# Output: 354224848179261915075
'''
