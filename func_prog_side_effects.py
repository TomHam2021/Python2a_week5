'''
# Complexity
# Functional programming reduces complexity by avoiding side-effects and mutable state

def side_effect():
    # här anropas oclså en global variable , inte func.programming
    global x
    x += 1


def mutate(xs):
    # här anropas extern variabel inneifrån en funktion, inte func.programming!
    xs.append(x)


x = 0
xs = []
mutate(xs)
side_effect()
print(xs)
# Output: [0] , x är ändrat!!

'''
# This is the same code but written in a functional style
# The print statement is now the only side effect


def no_side_effect(x):
    return x + 1


def no_mutation(xs, x):
    return [xs] + x


x = 0
xs = []
# här skapas en ny lista, inte ändra global variabel
with_x = no_mutation(xs, x)
# här skapas också en ny variabel med den nya datan
y = no_side_effect(x)

print(with_x)
# Output: [0]  , x är oförändrad
