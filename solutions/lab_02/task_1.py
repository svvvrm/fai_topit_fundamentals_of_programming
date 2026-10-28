# Эксперимент A
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))


# Эксперимент B
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

# Переназначение second на новый список
second = first.copy()

# Сравнение списков
print(first == second)
print(first is second)

# Изменение нового списка
second.append(40)

# Проверка
print(first, second)


# Дополнение
second = first.copy()

print(first == second)
print(first is second)

second.append(40)

print(first, second)


# Практическая задача
import copy

first_config = [
    "name 1",
    [
        "member 1",
        "member 2",
        "member 3"
    ],
    [
        "param1",
        "param2",
        "param3"
    ]
]

second_config = first_config
second_config[0] = "name 2"

print(first_config[0], second_config[0])

third_config = copy.deepcopy(first_config)

assert third_config is not first_config
assert third_config[1] is not first_config[1]
assert third_config[2] is not first_config[2]