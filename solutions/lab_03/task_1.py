import sys


def get_student_result(score: int, work_type: str, absences: int) -> dict:
    # input validation
    if not(0 <= score <= 100):
        print("Invalid value of student's grade")
        raise ValueError("Invalid value of student's grade")

    if not(0 <= absences <= 5):
        print("Invalid value of absences")
        raise ValueError("Invalid value of absences")

    # defining student's level
    levels = [
        "недостаточный",
        "удовлетворительный",
        "хороший",
        "отличный"
    ]

    if 90 <= score <= 100:
        student_level_index = 3

    elif 75 <= score <= 89:
        student_level_index = 2

    elif 60 <= score <= 74:
        student_level_index = 1

    elif score <= 59:
        student_level_index = 0

    if absences > 3 and student_level_index != 0:
        student_level_index -= 1

    # matching work type
    match work_type:
        case "exam":
            work_type_annotation = "экзаменационная работа"

        case "project":
            work_type_annotation = "проектная работа"

        case "practice":
            work_type_annotation = "практическая работа"

        case _:
            work_type_annotation = None

    return {
        "score_level": levels[student_level_index],
        "work_type_annotation": work_type_annotation 
    }


# retrieving data
score = int(input())
work_type = input()
absences = int(input())

try:
    student_result: dict = get_student_result(
        score=score,
        work_type=work_type,
        absences=absences
    )

    print(student_result["work_type_annotation"], student_result["score_level"])
except:
    sys.exit(1)


# testing
testing_data = [
    {
        "input": (100, "exam", 3),
        "expectation": {
            "work_type_annotation": "экзаменационная работа",
            "score_level": "отличный"
        }
    },
    {
        "input": (100, "exam", 4),
        "expectation": {
            "work_type_annotation": "экзаменационная работа",
            "score_level": "хороший"
        }
    },
    {
        "input": (90, "practice", 3),
        "expectation": {
            "work_type_annotation": "практическая работа",
            "score_level": "отличный"
        }
    },
    {
        "input": (89, "practice", 5),
        "expectation": {
            "work_type_annotation": "практическая работа",
            "score_level": "удовлетворительный"
        }
    },
    {
        "input": (75, "project", 0),
        "expectation": {
            "work_type_annotation": "проектная работа",
            "score_level": "хороший"
        }
    },
    {
        "input": (75, "project", 4),
        "expectation": {
            "work_type_annotation": "проектная работа",
            "score_level": "удовлетворительный"
        }
    },
    {
        "input": (74, "exam", 4),
        "expectation": {
            "work_type_annotation": "экзаменационная работа",
            "score_level": "недостаточный"
        }
    },
    {
        "input": (60, "exam", 2),
        "expectation": {
            "work_type_annotation": "экзаменационная работа",
            "score_level": "удовлетворительный"
        }
    },
    {
        "input": (59, "exam", 0),
        "expectation": {
            "work_type_annotation": "экзаменационная работа",
            "score_level": "недостаточный"
        }
    },
    {
        "input": (0, "exam", 5),
        "expectation": {
            "work_type_annotation": "экзаменационная работа",
            "score_level": "недостаточный"
        }
    },
]

for test in testing_data:
    student_result = get_student_result(*test["input"])

    assert student_result == test["expectation"]


input_data = [
    (100, "exam", 3),
    (100, "exam", 4),
    (90, "practice", 3),
    (89, "practice", 5),
    (75, "project", 0),
    (75, "project", 4),
    (74, "exam", 4),
    (60, "exam", 2),
    (59, "exam", 0),
    (0, "exam", 5)
]

levels_count = {
    "недостаточный": 0,
    "удовлетворительный": 0,
    "хороший": 0,
    "отличный": 0
}

for student in input_data:
    student_result = get_student_result(*student)

    levels_count[student_result["score_level"]] += 1

    print(f"{student_result['work_type_annotation']}: {student_result['score_level']}")

for level, count in levels_count.items():
    print(f'Отметка "{level}": {count}')