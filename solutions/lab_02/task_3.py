# Счетчик ссылок
import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


# Слабые ссылки
import weakref

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())


# Практическая задача
first = Record()
second = Record()
third = Record()

weak_dict = weakref.WeakValueDictionary()

weak_dict["first"] = first
weak_dict["second"] = second
weak_dict["third"] = third

del third

print(*weak_dict.keys())

del second

print(*weak_dict.keys())