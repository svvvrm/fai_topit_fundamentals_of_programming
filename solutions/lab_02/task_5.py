import sys
import tracemalloc

# Часть 1
empty_list = []
list_10 = list(range(390, 400))
tuple_10 = tuple(list(range(390, 400)))
string = "abcdefghij"
integer = 333

print("пустой список:", sys.getsizeof(empty_list), "байт")
print("список из десяти целых чисел:", sys.getsizeof(list_10), "байт")
print("кортеж:", sys.getsizeof(tuple_10), "байт")
print("строка из десяти символов:", sys.getsizeof(string), "байт")
print("целое число:", sys.getsizeof(integer), "байт")
print("объект None:", sys.getsizeof(None), "байт")


# Часть 2
arr = []
prev_size = sys.getsizeof(arr)

for i in range(100):
    arr.append(i)

    if sys.getsizeof(arr) != prev_size:
        print(f"Размер: {sys.getsizeof(arr)} байт")
        prev_size = sys.getsizeof(arr)

# Часть 3
import tracemalloc

tracemalloc.start()

numbers = list(range(100_000))

current, peak = tracemalloc.get_traced_memory()
print(f"текущее использование памяти: {(current / 1000):.2f} Кбайт")
print(f"пиковое использование памяти: {(peak / 1000):.2f} Кбайт")

tracemalloc.stop()
tracemalloc.start()

numbers = range(100_000)

current, peak = tracemalloc.get_traced_memory()
print(f"текущее использование памяти: {(current / 1000):.2f} Кбайт")
print(f"пиковое использование памяти: {(peak / 1000):.2f} Кбайт")

tracemalloc.stop()
