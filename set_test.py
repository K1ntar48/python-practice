
d = set()       # d = {} будет ошибкой так как создаст словарь


d = {"Apple", "Orange", "Peach", "Tomato"}

print(d)        # Выведет {'Tomato', 'Orange', 'Apple', 'Peach'}, что отличается последовательностью

e = set("library")
print(e)        # Удаляет все дубликаты значений

a = set('абракадабра')
b = set('алакозам')
print(a)                                  # уникальные буквы в a

print(a - b)                             # буквы в a, но не в b

print(a | b)                              # буквы в a или b, или в обоих

print(a & b)                                # буквы в a и b

print(a ^ b)                             # буквы в одном, но не в обоих


z = {x for x in 'абракадабра' if x not in 'абв'}
print(z)
