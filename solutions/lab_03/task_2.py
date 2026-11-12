import random
import time


measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

max_value = measurements[0]
min_value = measurements[0]
total = 0
length = 0
count_even = 0

for n in measurements:
    # sum of elements
    total += n

    # min value
    if n < min_value:
        min_value = n

    # max value
    if n > max_value:
        max_value = n

    # count even elements
    if n % 2 == 0:
        count_even += 1

    # length of array
    length += 1

average = total / length
count_gt_average = 0

for n in measurements:
    if n > average:
        count_gt_average += 1

result = (
    f"sum: {total}\n"
    f"min: {min_value}\n"
    f"max: {max_value}\n"
    f"even numbers: {count_even}\n"
    f"greater than average: {count_gt_average}"
)

print(result)


target = int(input("input number: "))

index = -1

for i in range(length):
    if measurements[i] == target:
        index = i
        break

print(f"index in measurements list: {index}")


# additional experiment
def is_prime(n: int):
    for divider in range(2, int(n**0.5) + 1):
        if n % divider == 0:
            return False

    return True


# practical extension
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

def binary_search(arr: list, target: int) -> tuple[int, int]:
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] > target:
            right = mid - 1
            comparisons += 1
        
        elif arr[mid] < target:
            left = mid + 1
            comparisons += 1

        else:
            return mid, comparisons

    return -1, comparisons

def linery_search(arr: list, target: int) -> tuple[int, int]:
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


for n in (10, 100, 1000):
    arr = [random.randint(-10**5, 10**5) for _ in range(n)]
    arr.sort()

    binary_start = time.perf_counter()
    binary_comparisons = binary_search(arr, 10**6)[1]
    binary_time = f"{((time.perf_counter() - binary_start) * 1000):.3f} мс"

    linery_start = time.perf_counter()
    linery_comparisons = linery_search(arr, 10**6)[1]
    linery_time = f"{((time.perf_counter() - linery_start) * 1000):.3f} мс"

    print(f"n = {n}")
    print(" _____________________________________________")
    print("|             | binary search | linery search |")
    print("|-------------|---------------|---------------|")
    print(f"|    time     |{binary_time:^15}|{linery_time:^15}|")
    print(f"| comparisons |{binary_comparisons:^15}|{linery_comparisons:^15}|")
    print("|_____________|_______________|_______________|\n")

