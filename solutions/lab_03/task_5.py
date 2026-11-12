def mean(values: list[int | float]) -> float:
    return sum(values) / len(values)


def minimum(values: list[int | float]) -> int | float:
    min_value = values[0]

    for value in values:
        if min_value > value:
            min_value = value

    return min_value


def maximum(values: list[int | float]) -> int | float:
    max_value = values[0]

    for value in values:
        if max_value < value:
            max_value = value

    return max_value


def find_top_students(student_data: dict) -> list[str]:
    scores = [summary["score"] for summary in student_data if summary["score"] != "отсутствует"]

    if not scores:
        return []
    
    best_score = maximum([summary["score"] for summary in student_data if summary["score"] != "отсутствует"])
    best_students = []

    for summary in student_data:
        if summary["score"] == best_score:
            best_students.append(summary["name"])

    return best_students


def get_mean_result(student_data: dict) -> float:
    results = []

    for summary in student_data:
        if summary["score"] != "отсутствует":
            results.append(summary["score"])

    if not results:
        return "отсутствует"

    return mean(results)


def get_max_result(student_data: dict) -> float:
    results = []

    for summary in student_data:
        if summary["score"] != "отсутствует":
            results.append(summary["score"])

    if not results:
        return "отсутствует"

    return maximum(results)


def get_min_result(student_data: dict) -> float:
    results = []

    for summary in student_data:
        if summary["score"] != "отсутствует":
            results.append(summary["score"])

    if not results:
        return "отсутствует"

    return minimum(results)


def count_categories(student_data: list[dict]) -> dict:
    result = {
        "недостаточный": 0,
        "удовлетворительный": 0,
        "хороший": 0,
        "отличный": 0
    }

    for summary in student_data:
        result[summary["result"]] += 1

    return result


def classify(score: int | float) -> str:
    if 90 <= score <= 100:
        return "отличный"

    elif 75 <= score <= 89:
        return "хороший"
    
    elif 60 <= score <= 74:
        return "удовлетворительный"
    
    elif score <= 59:
        return "недостаточный"


def student_summary(name: str, results: list[int]) -> dict:
    """Создает словарь со статистикой и результатами студента

    Args:
        name: строка с именем студента
        results: список с баллами студента за несколько работ, может быть пустым
    
    Returns:
        Словарь со следующей структурой:
            * ключ "name": имя студента, str
            * ключ "best score": максимальный балл, float
            * ключ "worst score": минимальный балл, float
            * ключ "score": итоговый балл (ср. арифмет. всех баллов), float
            * ключ "result": категория результата, str
            * ключ "results": список с баллами студента за несколько работ, list[int]

    Raises:
        ValueError: если name cтрока, если results не список, если в results хранится не int
    """
    # validation
    if not isinstance(name, str):
        raise ValueError("name must be string")

    if not isinstance(results, list):
        raise ValueError("results must be list")

    for value in results:
        if not isinstance(value, int):
            raise ValueError("results list elements must be integer")

    # main logic
    if not results:
        return {
            "name": name,
            "best score": "отсутствует",
            "worst score": "отсутствует",
            "score": "отсутствует",
            "result": "недостаточный",
            "results": []
        }
    
    results_mean = mean(results)

    return {
        "name": name,
        "best score": maximum(results),
        "worst score": minimum(results),
        "score": results_mean,
        "result": classify(results_mean),
        "results": results.copy()
    }


def group_summary(student_data: list[dict]) -> dict:
    """Создает словарь со статистикой и результатами группы

    Args:
        student_data: Список словарей со следующей структурой:
            * ключ "name": имя студента, str
            * ключ "best score": максимальный балл, float
            * ключ "worst score": минимальный балл, float
            * ключ "score": итоговый балл (ср. арифмет. всех баллов), float
            * ключ "result": категория результата, str
            * ключ "results": список с баллами студента за несколько работ, list[int]
            
    
    Returns:
        Словарь со следующей структурой:
            * ключ "best score": макс средний балл (float), либо "отсутствует" у всех студентов нет баллов (str)
            * ключ "worst score": мин средний балл (float), либо "отсутствует" у всех студентов нет баллов (str)
            * ключ "mean score": ср.арифмет. средних баллов (float), либо "отсутствует" у всех студентов нет баллов (str)
            * ключ "top students": список имен студентов с максимальным баллом, list[str]
            * ключ "category 1": кол-во студентов с отметкой "отлично", int
            * ключ "category 2": кол-во студентов с отметкой "хорошо", int
            * ключ "category 3": кол-во студентов с отметкой "удовлетворительно", int
            * ключ "category 4": кол-во студентов с отметкой "неудовлетворительный", int

    Raises:
        ValueError: если student_data не list
    """
    # validation
    if not isinstance(student_data, list):
        raise ValueError("student_data must be list")

    # main logic
    if not student_data:
        return {
            "best score": "отсутствует",
            "worst score": "отсутствует",
            "mean score": "отсутствует",
            "top students": [],
            "category 1": 0,
            "category 2": 0,
            "category 3": 0,
            "category 4": 0
        }

    categories = count_categories(student_data=student_data)

    return {
        "best score": get_max_result(student_data),
        "worst score": get_min_result(student_data),
        "mean score": get_mean_result(student_data),
        "top students": find_top_students(student_data),
        "category 1": categories["отличный"],
        "category 2": categories["хороший"],
        "category 3": categories["удовлетворительный"],
        "category 4": categories["недостаточный"]
    }




def format_report(student_data: list[dict], group_data: dict) -> str:
    """Создает словарь со статистикой и результатами группы

    Args:
        student_data: Список словарей со следующей структурой:
            * ключ "name": имя студента, str
            * ключ "best score": максимальный балл, float
            * ключ "worst score": минимальный балл, float
            * ключ "score": итоговый балл (ср. арифмет. всех баллов), float
            * ключ "result": категория результата, str
            * ключ "results": список с баллами студента за несколько работ, list[int]
        group_data: Словарь со следующей структурой:
            * ключ "best score": макс средний балл (float), либо "отсутствует" у всех студентов нет баллов (str)
            * ключ "worst score": мин средний балл (float), либо "отсутствует" у всех студентов нет баллов (str)
            * ключ "mean score": ср.арифмет. средних баллов (float), либо "отсутствует" у всех студентов нет баллов (str)
            * ключ "top students": список имен студентов с максимальным баллом, list[str]
            * ключ "category 1": кол-во студентов с отметкой "отлично", int
            * ключ "category 2": кол-во студентов с отметкой "хорошо", int
            * ключ "category 3": кол-во студентов с отметкой "удовлетворительно", int
            * ключ "category 4": кол-во студентов с отметкой "неудовлетворительный", int
            
    
    Returns:
        Текст отчета, str

    Raises:
        ValueError: если student_data не list, если group_data не dict
    """
    # validation
    if not isinstance(student_data, list):
        raise ValueError("student_data must be list")

    if not isinstance(group_data, dict):
        raise ValueError("group_data must be list")
    
    # main logic
    student_report = group_report = ""
    rating = "============== Рейтинг ===============\n"

    # forming student reports
    for summary in student_data:
        if summary["score"] == "отсутствует":
            student_report += (
                f"============== Студент ===============\n"
                f"Имя: {summary["name"]}\n"
                f"Лучший балл: {summary["best score"]}\n"
                f"Худший балл: {summary["worst score"]}\n"
                f"Средний балл: {summary["score"]}\n"
                f"Результат: {summary["result"]}\n\n"
            )

        else:
            student_report += (
                f"============== Студент ===============\n"
                f"Имя: {summary["name"]}\n"
                f"Лучший балл: {summary["best score"]:.2f}\n"
                f"Худший балл: {summary["worst score"]:.2f}\n"
                f"Средний балл: {summary["score"]:.2f}\n"
                f"Результат: {summary["result"]}\n\n"
            )

    # forming rating
    non_empty_students = [student for student in student_data if student["score"] != "отсутствует"]
    empty_students = [student for student in student_data if student["score"] == "отсутствует"]

    for summary in sorted(non_empty_students, key=lambda x: x["score"], reverse=True):
        rating += f"{summary['name']}: {summary['score']:.2f} баллов\n"

    for summary in empty_students:
        rating += f"{summary['name']}: баллы отсутствуют\n"

    # forming group report
    group_report = (
        f"============== Группа  ===============\n"
        f"Лучший балл: {group_data["best score"]}\n"
        f"Худший балл: {group_data["worst score"]}\n"
        f"Средний балл: {group_data["mean score"]}\n"
        f"Лучшие студенты: {", ".join(group_data["top students"])}\n"
        f"Кол-во 'отлично': {group_data["category 1"]}\n"
        f"Кол-во 'хорошо': {group_data["category 2"]}\n"
        f"Кол-во 'удовлетворительно': {group_data["category 3"]}\n"
        f"Кол-во 'недостаточно': {group_data["category 4"]}\n\n"
    )

    return student_report + group_report + rating


def main(students: dict) -> None:
    student_data = [student_summary(name=name, results=students[name]) for name in students]
    group_data = group_summary(student_data=student_data)
    report = format_report(
        student_data=student_data,
        group_data=group_data
    )

    print(report)


students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
    "dgas": []
}

# main(students=students)


# test
scenarios = {
    "regular": {
        "Анна": [78, 91, 84, 88],
        "Борис": [60, 72, 68],
        "Дарья": [95, 93, 97, 90],
        "Илья": [55, 61],
    },
    "one student": {
        "Илья": [55, 61]
    },
    "two best students": {
        "Анна": [78, 91, 84, 88],
        "Валерия": [78, 91, 84, 88]
    },
    "empty group": {

    },
    "student with no result": {
        "Анна": []
    },
    "threshold category values":{
        "Анна": [90, 90, 90, 90],
        "Иван": [89, 89]
    }
}


for scenario in scenarios:
    print()
    print("Test: ", scenario)
    print()

    main(students=scenarios[scenario])

    input("press any button to continue: ")