"""Программа для расчёта характеристик экспериментальных запусков."""


name = input("Введите название эксперимента: ")
researcher = input("Введите имя исследователя: ")
starts = int(input("Введите кол-во запусков: "))
duration = float(input("Введите длительность одного запуска: "))
real = float(input("Введите действительную часть комплексного коэффициента: "))
imag = float(input("Введите мнимую часть комплексного коэффициента: "))


gen_duration_sec = starts * duration
gen_duration_min = gen_duration_sec / 60
complex_number = complex(real, imag)
modulus = real ** 2 + imag ** 2
has_runs = bool(starts)


print(
    f"========================================\n"
    f"ЭКСПЕРИМЕНТ: {name}\n"
    f"Исследователь: {researcher}\n"
    f"Запуски: {starts}\n"
    f"Общее время: {gen_duration_sec:.2f} с ({gen_duration_min:.2f} мин)\n"
    f"Коэффициент: {complex_number}\n"
    f"Квадрат модуля: {modulus:.2f}\n"
    f"Есть выполненные запуски: {has_runs}\n"
    f"========================================\n"
)

print(
    f"Название: {type(name).__name__}, "
    f"Имя исследователя: {type(researcher).__name__}, "
    f"Кол-во запусков: {type(starts).__name__}, "
    f"Длительность: {type(duration).__name__}, "
    f"Действ. часть: {type(real).__name__}, "
    f"Мнимая часть: {type(imag).__name__}"
)