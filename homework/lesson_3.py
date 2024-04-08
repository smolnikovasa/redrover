
"""Задание 3.1."""
# Вариант 1
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

# Вариант 2
print(*my_list[2], sep='\n')


"""Задание 3.2."""
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(f"Сумма всех чисел: {sum([x for x in list_1 if isinstance(x, int) or isinstance(x, float)])}")
print(f"Все строки, где есть буква 'a': {[x for x in list_1 if isinstance(x, str) and 'a' in x]}")


"""Задание 3.3."""
print(tuple(['cat', 'dog', 'horse', 'cow']))


"""Задание 3.4."""
family_1 = tuple(input('Введите членов первой семьи через запятую: ').split(','))
family_2 = tuple(input('Введите членов второй семьи через запятую: ').split(','))
if len(family_1) == len(family_2):
    print('Состав аналогичный')
elif len(family_1) > len(family_2):
    print('Семья 1 больше')
else:
    print('Семья 2 больше')


"""Задание 3.5."""
film = {
    "title": "чебурашка",
    "director": "Дед Гена защищает чудо-зверя от дамы со скверным характером",
    "year": 2022,
    "budget": 850000000,
    "main_actor": "Сергей Гармаш"
}
print(*film.keys(), sep=", ")
print(*film.values(), sep=", ")
print([f"{x} -{y}" for x, y in film.items()], sep=", ")


"""Задание 3.6."""
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))


"Задание 3.7."
my_set = set([1, 2, 3, 4, 5, 3, 2, 1])
print(my_set)

"Задание 3.8."
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))
