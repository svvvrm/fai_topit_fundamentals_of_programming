a = 1000
b = a
c = int("1000")
# c = None

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)    # True
print("a is b:", a is b)    # True
print("a == c:", a == c)    # True
print("a is c:", a is c)    # False

# # True expected
# print("c is None:", c is None)

first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)