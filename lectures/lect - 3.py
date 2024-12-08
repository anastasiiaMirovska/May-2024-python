# class User(object):
#     # __slots__ = ('name', 'age')
#     _count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#
#     def set_name(self, name):
#         self.__name = name
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     name = property(fget=get_name, fset=set_name)
#
#
# user1 = User("Bob", 12)
# print(user1.name)


class User(object):
    # __slots__ = ('name', 'age')
    _count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.name
    def __str__(self):
        return str(self.__dict__)



user1 = User("Bob", 12)
print(user1.name)


class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)

    def __len__(self):
        return len(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, key):
        return self.__arr[key]

    def __delitem__(self, key):
        del self.__arr[key]

    def push(self, item):
        self.__arr.append(item)

    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])

    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])



arr = Array(1, 2, 3, 4)
arr.push(5)
print(arr)

arr[2]=0
print(arr[2])
del arr[0]
print(arr)

map_arr = arr.map(lambda item: item**2)
print(map_arr)


filter_arr = arr.filter(lambda item: item<6)
print(filter_arr)