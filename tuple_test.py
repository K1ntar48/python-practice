tup = 3, 7
print(type(tup))

a, b = tup
print(a,b)

one = (5,)
print(type(one))            # tuple
print(type((5)))            # int — вот ловушка!

def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 1, 9, 2])
print(lo, hi)               # 1 9

