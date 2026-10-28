# Эксперимент А

x = 17
y = 5

print(x + y, type(x + y))    # 22, int
print(x - y, type(x - y))    # 12, int
print(x * y, type(x * y))    # 85, int
print(x / y, type(x / y))    # 3.4, float
print(x // y, type(x // y))  # 3, int
print(x % y, type(x % y))    # 2, int
print(x ** y, type(x ** y))  # 1419857, int


# Эксперимент B

print(2 ** 1000)


# Эксперимент C
import math 

result = 0.1 + 0.2

print(result)
print(result == 0.3)
print(result - 0.3)
print(math.isclose(result, 0.3))


# Эксперимент D

print(int("42"), type(int("42")))    # 42, int
print(float("3.14"), type(float("3.14"))) # 3.14, float
print(str(2026), type(str(2026)))    # 2026, str
print(bool(0), type(bool(0)))        # False, bool
print(bool(-1), type(bool(-1)))      # True, bool
print(bool(""), type(bool("")))      # False, bool
print(bool("False"), type(bool("False"))) # True, bool
print(
	complex(2, -3).real,   # 2.0
	complex(2, -3).imag,   # -3.0
    type(complex(2, -3))   # complex
)