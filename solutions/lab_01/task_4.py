student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[0])    # первый символ имени
print(student[3])    # последний символ имени
print(student[:4])   # срез с именем Анна
print(student[5:])   # срез с фамилией Смирнова
print(student.upper())  # student в врехнем регистре
print(student.lower())  # student в нижнем регистре
print(student[0] + "." + student[5] + ".") # инициалы
print(course[::-1])  # название курса наоборот

text1 = "%s — %s: %d/%d (%.1f%%)" % (
    student,
    course,
    completed,
    total,
    (completed / total) * 100
)
print(text1)

text2 = "{} — {}: {}/{} ({}%)".format(
    student,
    course,
    completed,
    total,
    (completed / total) * 100
)
print(text2)

text3 = (
    f"{student} — {course}: "
    f"{completed}/{total} "
    f"({(completed / total) * 100}%)"
)     
print(text3)


# unicode
symbol = "Я"
print(symbol)    
print(ord(symbol))
print(chr(ord(symbol))) 
print(symbol.encode("utf-8"))
print(len(symbol.encode("utf-8")))


# text4 = "fffff"
# text4[0] = "g"