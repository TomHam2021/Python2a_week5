# Subscriptable map
# • The built-in map is not subscriptable
# • Here is a possible implementation
# Subscriptable = man kan hämta data för ett specivikt element i listan

class SubscriptableMap:
    def __init__(self, f, iterable):
        self._mapped = map(f, iterable)
        # ovan så skapas listan -->  [0, 2, 4, 6, 8] dvs x * 2 för range(5) = 0..4
        # print(list(self._mapped))
        self._memo = []

    # "dunder" = "__" detta anger att man kan hämta ett specifict index
    # här skapas listan self._memo varje gång man anropar med ett index!
    def __getitem__(self, index):
        # efter försa anropet är _memo = [0,2] --> len = 2
        # anda anropet är index = 2 och len = 2 --> lätt till 3:an
        # för det 3dje anropet är index =1 och len = 3 --> hoppa direkt till return raden!
        while index >= len(self._memo):
            # detta körs bara om len(_memo) är mindre än index, dvs behöver skapa fler element
            self._memo.append(next(self._mapped))
        return self._memo[index]

    def __str__(self):
        # self._memo = [*self._memo, *self._mapped]
        # return f"SubscriptableMap({self._memo})"
        # nedan funka lika bra som ovan.
        return f"SubscriptableMap({list(self._mapped)})"


mymap = SubscriptableMap(lambda x: x * 2, range(5))
# Subscriptable = man kan hämta data för ett specifikt element i listan tex [1]
print(mymap[1], mymap[2], mymap[1])
#  Output: 2, 4

# x = [1,2,3]
# print(*x)   # "*" ger varje element i listan
# Output = 1 2 3

print(SubscriptableMap(lambda x: x * 2, range(5)))
# obs att här skapas ett nytt object av 'SubscriptableMap' och listan _memo = []
#  Output: SubscriptableMap([0, 2, 4, 6, 8])
