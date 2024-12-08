from typing import Callable, Tuple


# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

def note():
    todo_list = []
    def add_todo(task):
        nonlocal todo_list
        todo_list.append(task)
    def get_all():
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all

add_todo1, get_all1 = note()
add_todo2, get_all2 = note()
add_todo1("Say Hello!")
add_todo2("Hello!")
print(get_all1())
print(get_all2())

# 2) протипізувати перше завдання


def note() -> Tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(task: str) -> None:
        nonlocal todo_list
        todo_list.append(task)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all

add_todo1, get_all1 = note()
add_todo2, get_all2 = note()
add_todo1("Say Hello!")
add_todo2("Hello!")
print(get_all1())
print(get_all2())

# 3) створити функцію котра буде повертати суму розрядів числа у вигляді строки (також використовуємо типізацію)

# Перший спосіб
# def expanded_form(num: int) -> str:
#     number = str(num)
#     num_length = len(number)
#     digits:list[str] = []
#     for i in range(num_length, 0, -1):
#         degree = 10**(i-1)
#         digit = (num//degree)*degree
#         digits.append(str(digit))
#         num -= digit
#     return " + ".join(digits)

# Другий спосіб
def expanded_form(num: int) -> str:
    st = str(num)
    length = len(st)-1
    res = []
    for i, ch in enumerate(st):
        if ch!=0:
            res.append(ch+'0'*(length-i))
    return ' + '.join(res) + f' = {num}'


print(expanded_form(4287))
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій


def count_call(foo):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        foo(*args, **kwargs)
        print(f"Function \"{foo.__name__}\" was called {count} times")

    return inner

@count_call
def greeting(name: str):
    print(f"Hello {name}")

greeting("Oles")
greeting("Oles")