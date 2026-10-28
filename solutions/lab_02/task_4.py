import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

# вывод текущего состояния автоматического сборщика мусора
print(gc.isenabled())
# вывод порогов поколений
print(gc.get_threshold())
# вывод статистики поколений
print(gc.get_stats())

first_id, second_id = id(first), id(second)

del first, second

collected = gc.collect()
print(collected)


# дополнительный эксперимент
gc.disable()

class Note:
    pass

a, b = Note(), Note()
a.other, b.other = b, a

list_1, list_2 = [], []
list_1.append(list_2)
list_2.append(list_1)

del a, b, list_1, list_2

print(gc.collect())

gc.enable()


# практическая задача
before = gc.collect()
print(before)

a = {"name": "A", "links": []}
b = {"name": "B", "links": []}
c = {"name": "C", "links": []}
d = {"name": "D", "links": []}

a["links"].append(b)
b["links"].append(c)
c["links"].append(a)

print("A ->", a["links"][0]["name"])
print("B ->", b["links"][0]["name"])
print("C ->", c["links"][0]["name"])
print("D не имеет связей: ", d["links"] == [])

del a
del b
del c

after = gc.collect()
print(after)