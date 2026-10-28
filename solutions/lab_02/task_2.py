import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

def log_lists_state() -> None:
    log_message = (
        f"original: {original}\n"
        f"    id(original):   {id(original)}\n"
        f"    id(original[0]):   {id(original[0])}\n"
        f"    id(original[0][1]):   {id(original[0][1])}\n\n"
        f"alias: {alias}\n"
        f"    id(alias):   {id(alias)}\n"
        f"    id(alias[0]):   {id(alias[0])}\n"
        f"    id(alias[0][1]):   {id(alias[0][1])}\n\n"
        f"shallow: {shallow}\n"
        f"    id(shallow):   {id(shallow)}\n"
        f"    id(shallow[0]):   {id(shallow[0])}\n"
        f"    id(shallow[0][1]):   {id(shallow[0][1])}\n\n"
        f"deep: {deep}\n"
        f"    id(deep):   {id(deep)}\n"
        f"    id(deep[0]):   {id(deep[0])}\n"
        f"    id(deep[0][1]):   {id(deep[0][1])}\n\n"
    )

    print(log_message)

# Изменение 1
original.append(["Databases", 5])
log_lists_state()

# Изменение 2
original[0][1] = 3
log_lists_state()


# Исследование матрицы
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1

print(wrong_matrix)
print(correct_matrix)