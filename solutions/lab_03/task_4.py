def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""

    assert isinstance(values, list), "values must be list"

    assert len(values) > 0, "values length must be positive"

    for x in values:
        assert isinstance(x, float), "values list must contain only float numbers"

    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""

    # validation
    assert isinstance(name, str)

    name: list[str] = name.split()

    assert 1 <= len(name) <= 3

    for part in name:
        assert part.isalpha()

    # main logic
    for i in range(len(name)):
        name[i] = name[i].capitalize()

    return " ".join(name)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""

    # validation
    assert isinstance(student, str)
    assert isinstance(precision, int)
    assert isinstance(prefix, str)
    for x in results:
        assert isinstance(x, int)

    # preparing data
    results = [float(x) for x in results]
    result = arithmetic_mean(results)
    name: str = normalize_name(student)

    # building report
    report = (
        f"Студент: {name}\n"
        f"{prefix}: {result:.{precision}f}"
    )

    return report


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""

    # validation
    assert tags

    for tag in tags:
        assert isinstance(tag, str)

    assert isinstance(lowercase, bool)

    # choosing correct unique tags
    result = []
    unique_tags = set()

    for tag in tags:
        tag = tag.lower() if lowercase else tag

        if tag != "" and tag not in unique_tags:
            result.append(tag)
            unique_tags.add(tag)

    return tuple(result)


testing_data = {
    "arithmetic_mean": [
        {
            "input": [1.0, 2.0, 3.0],
        },
    ],
    "normalize_name": [
        {
            "input": "   Антон иванович   чигур ",
        },
    ],
    "build_report": [
        {
            "input": {
                "positional": [
                    "   Антон иванович   чигур ",
                    [5, 4, 5, 4, 3]
                ],
                "keyword": {
                    "precision": 3,
                    "prefix": "Балл"
                }
            },
        },
    ],
    "collect_tags": [
        {
            "input": {
                "positional": [
                    ["tag1", "tag2", "tAG3"]
                ],
                "keyword": {
                    "lowercase": False
                }
            }
        }
    ]
}


arithmetic_mean_output = arithmetic_mean(
    values=testing_data["arithmetic_mean"][0]["input"]
)
print(arithmetic_mean_output)

normalize_name_output = normalize_name(
    name=testing_data["normalize_name"][0]["input"]
)
print(normalize_name_output)

build_report_output = build_report(
    *testing_data["build_report"][0]["input"]["positional"],
    **testing_data["build_report"][0]["input"]["keyword"]
)
print(build_report_output)

collect_tags_output = collect_tags(
    *testing_data["collect_tags"][0]["input"]["positional"][0],
    **testing_data["collect_tags"][0]["input"]["keyword"]
)
print(collect_tags_output)


# LEGB research
course = "Python"

def outer():
    course = "Advanced"

    def inner():
        nonlocal course
        course = "Basic"

    print(course)

    inner()

    print(course)

outer()

print(course)


# changeable default value
def add_result(value, results=[]):
    results.append(value)
    return results

print(add_result(3))
print(add_result(4))


# practical extension
def apply_to_results(operation, values):
    result = []

    for value in values:
        result.append(operation(value))

    return result

# named function
def double(x: int | float) -> int | float:
    return 2 * x

data = [4, 6, 2, 7.0, 10]

print(f"Named function: {apply_to_results(double, data)}")
print(f"Lambda function: {apply_to_results(lambda x: x * 2, data)}")

def make_threshold_checker(threshold):
    def inner(value):
        return value >= threshold

    return inner

is_gt_10 = make_threshold_checker(10)
is_gt_100 = make_threshold_checker(100)

print(f"Checker 10: {is_gt_10(30)}")
print(f"Checker 100: {is_gt_100(30)}")
