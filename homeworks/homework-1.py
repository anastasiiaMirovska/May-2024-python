# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# My variant
st = 'as 23 fdfdg544'
number_array = []
for char in st:
    if char.isnumeric():
        number_array += char
result = ','.join(number_array)
print(result)

# Resolve
st = 'as 23 fdfdg544'
print(', '.join(num for num in st if num.isnumeric()))


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################

# My variant
st = 'as 23 fdfdg544 34'
number_array = []
i = 0
while i < len(st):
    if st[i].isnumeric():
        number = st[i]
        i += 1
        while i < len(st) and st[i].isnumeric():
            number += st[i]
            i += 1
        number_array.append(number)
    else:
        i += 1

result = ','.join(number_array)
print(result)

# Resolve
st = 'as 23 fdfdg544 34'
print(', '.join(''.join(ch if ch.isnumeric() else ' ' for ch in st).split()))

# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
print([ch.upper() for ch in greeting])


# 2) з діапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

print([number ** 2 for number in range(50) if number % 2 != 0])

# function
#
# - створити функцію яка виводить ліст


def print_list(my_list) -> None:
    for i in my_list:
        print(i, end=' ')


l = ['apple', 'banana', 'cherry']
print_list(l)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.


def find_max(a:int|float, b:int|float, c:int|float) -> int|float:
    # Перший спосіб
    # max_number = a if a > b else b
    # if max_number < c:
    #     max_number = c
    # print(f'\nThe maximum number is {max_number}')
    # return max_number
    # Другий спосіб
    res = max(a,b,c)
    print(res)
    return res


numbers = [2,7,1]
find_max(*numbers)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
l = [1,6,3,4,2,8,9,0,11]


def min_max(*args):
    print(max(args))
    return min(args)


print(min_max(*l))

# - створити функцію яка повертає найбільше число з ліста
def max_from_list(list_):
    return max(list_)


print(max_from_list(l))

# - створити функцію яка повертає найменше число з ліста
def min_from_list(list_):
    return min(list_)


print(min_from_list(l))
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_of_list(list_):
    return sum(list_)


print(sum_of_list(l))
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def find_average(list_):
    return round(sum(list_)/len(list_),2)


print(find_average(l))


# ################################################################################################
# 1)Дано list:
my_list = [22, 3,5,2,8,2,-23, 8,23,5]


#   - знайти мін число
def min_of_list(list_):
    print(f"Мінімальне число в списку = {min(list_)}")


#   - видалити усі дублікати
def del_duplicates(list_):
    # Перший варіант
    # new_list = []
    # for number in list_:
    #     if number in new_list:
    #         continue
    #     else:
    #         new_list.append(number)
    # print(f"Змінений список: {new_list}")
    # return new_list

    # Другий варіант
    new_list = list(set(list_))
    print(f"Змінений список: {new_list}")
    return new_list


#   - замінити кожне 4-те значення на 'X'
def substitute_fourth_by_x(list_):
    # Перший варіант
    # for num in range(3,len(list_), 4):
    #     list_[num] = 'X'
    # print(f"Змінений список: {list_}")
    # return list_

    # Другий варіант
    print(['X' if not (i + 1) % 4 else item for i, item in enumerate(list_)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(side_size):
    for i in range(0, side_size):
        if i==0 or i==side_size-1:
            print(side_size * '*')
        else:
            print("*"+" "*(side_size-2)+"*")



# 3) вивести табличку множення за допомогою циклу while
def multiplication_table():
    size = 9
    i = 1
    while i <= size:
        n = 1
        while n <= size:
            # Перший спосіб
            # number = str(i*n)
            # print(str(number)+" "*(4-len(number)), end="")

            # Другий спосіб
            # res = i*n
            # print(" " if res//10 else "  ", end="")
            # print(res, end="")

            # Третій спосіб
            res = i * n
            print(f'{res:4}', end="")
            n += 1
        print()
        i += 1


# 4) переробити це завдання під меню
def menu():
    print("1 -- Знайти мінімальне число")
    print("2 -- Видалити усі дублікати")
    print("3 -- Замінити кожне 4-те значення на 'X'")
    print("4 -- Вивести на екран пустий квадрат з '*'")
    print("5 -- Bивести табличку множення")
    print("6 -- Вихід")


play = True
while play:
    menu()
    choice = int(input("Виберіть опцію: "))
    match choice:
        case 1: min_of_list(my_list)
        case 2: my_list = del_duplicates(my_list)
        case 3: my_list = substitute_fourth_by_x(my_list)
        case 4:
            side_size = int(input("Введіть розмір сторони квадрата: "))
            square(side_size)
        case 5:
            multiplication_table()
        case 6:
            print("Дякую за увагу!")
            play = False
        case _:
            print("Неправильно введена опція. Спробуйте ще раз.")

