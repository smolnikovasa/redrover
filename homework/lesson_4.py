from math import sqrt
from functools import reduce
from datetime import datetime
import time


"Задание 4.1."
def square(side):
  return (side**2, side*4, round(sqrt(side**2*2), 2))



"Задание 4.2."
def employee(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

employee(last_name='Смольникова', name='Светлана', age=42, position='тестировщик')

"Задание 4.3."
my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x > 0, my_list)))


"Задание 4.4."
print(reduce(lambda x, y: x*y, my_list))


"Задание 4.5."
def count_execution_time(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        end = datetime.now()
        exec_time = end - start

        print(f'{func.__name__} выполняется: {exec_time}')
        return result
    return wrapper

def my_decorater(func):
    def wrapper(*args):
        print("Выполняется декоратор")
        print("А теперь выполняется функция")
        result = func(*args)
        print('Завершилось выполнение')
        return result
    return wrapper


@my_decorater
@count_execution_time
def greeting(name):
    time.sleep(5)
    print_str = f'Привет {name}!'
    print(print_str)
    return print_str

name = input("Введите имя")
print(greeting(name))
