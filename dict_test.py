book = {'title': 'Shooter', 'genre': 'Action', 'author': 'Steven King', 'year': 2012}
book['year'] = 2013
book['publisher'] = 'Penguin'       #Если такого ключа нет, то он создается
print(book)

print(book['title'])                #Выведет Shooter

del book['publisher']                 #Удаляет ключ и значение

print(list(book))                          #Выведет ['title', 'genre', 'author', 'year'] — список ключей словаря

print(sorted(book))                        #Выведет ['author', 'genre', 'title', 'year'] — отсортированный список ключей словаря

print('genre' in book)                  #Выведет True, так как ключ 'genre' есть в словаре

print('publisher' in book)              #Выведет False, так как ключа 'publisher' нет в словаре

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))   #Конструктор dict() создает словарь из списка кортежей

print({x: x**2 for x in (2, 4, 6)})            #Выведет {2: 4, 4: 16, 6: 36} — словарь, где ключи — числа из кортежа, а значения — их квадраты


odds = {i: i**2 for i in (1, 3, 5)}
evens = {i: i**2 for i in (2, 4, 6)}
print({**odds, **evens})                       #Выведет {1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36} — объединение двух словарей в один


book = {'title': 'Shooter', 'genre': 'Action', 'author': 'Steven King', 'year': 2013}

# 1. .get() — безопасный доступ
print(book.get('title'))          # Shooter
print(book.get('publisher'))      # None (не KeyError!)
print(book.get('publisher', '—')) # '—' (дефолт)

# 2. Перебор
print(book.keys())                # dict_keys([...])
print(book.values())              # dict_values([...])
print(book.items())               # dict_items([...])

for key, value in book.items():
    print(key, '→', value)

# 3. .update() — слияние
extra = {'publisher': 'Penguin', 'pages': 300}
book.update(extra)
print(book)

# 4. .setdefault() — добавить, только если ключа нет
book.setdefault('genre', 'Unknown')   # 'Action' уже есть, не меняется
book.setdefault('language', 'en')     # добавляется

# 5. .pop() — удалить и вернуть значение
pages = book.pop('pages')
print(pages)                      # 300

# 6. KeyError — увидь своими глазами
try:
    print(book['nonexistent'])
except KeyError:
    print("Ключа нет")